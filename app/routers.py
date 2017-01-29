from re import match
from os import getcwd
from bottle import static_file
from zope.component import getUtility
from libs.output import ITemplate
from actions import Application
from bottle import route,static_file,request,response,get,post,error,redirect
from json import dumps

from os import rmdir,mkdir,unlink,walk
from os.path import exists
from os import sep

@get('/js/<filename>')
def JSFiles(filename):
    return static_file(filename,getcwd()+sep+'static'+sep+'js')

@get('/img/<filename>')
def IMGFiles(filename):
    return static_file(filename,getcwd()+sep+'static'+sep+'img')

@get('/login')
def BLogin():
    if not request.is_xhr:
        if Application().Tasks(['Users','checkExist'])[0]:
            return getUtility(ITemplate).render('login.tpl',{'eflag':False,'emsg':None,'setpass':False})
        
        else:
            redirect('/newpass')

@get('/newpass')
def NLogin():
    if not request.is_xhr:
        return getUtility(ITemplate).render('login2.tpl',{'eflag':False,'emsg':None,'setpass':True})

@get('/backend')
def Backend():
    if not request.is_xhr:
        codes = Application().Tasks(('DataMNG','Get','ListCodes'))
        return getUtility(ITemplate).render('backend.tpl',{'codes':Application().Tasks(('DataMNG','Get','ListCodes')),'cid':[False,None]})
    
    else:
        #Session Request hier [False,None,None]
        response.set_header('X-Requested-With','XMLHttpRequest')
        response.set_header('Content-Type','application/json')        
        
        if 'atype' in request.query.keys():
            if 'newkey' == request.query['atype']:
                nentry = Application().Tasks(('DataMNG','Set','NewEntry'))
                if not exists(getcwd()+sep+'upload'+sep+nentry):
                    mkdir(getcwd()+sep+'upload'+sep+nentry)
                return dumps([True,True,nentry])
            
            else:
                return dumps([True,False,None])

@get('/backend/code/<cid>')
def GBackendCode(cid):
    if not request.is_xhr:
        dinfo = Application().Tasks(('DataMNG','Get','CodeDetails',cid))[1]
        #Session JA        
        return getUtility(ITemplate).render('backend.item.tpl',{
            'codes':Application().Tasks(('DataMNG','Get','ListCodes')),
            'cid':[True,cid],
            'dinfo':[dinfo.keys(),dinfo,len(dinfo.keys())]
        })
    
    else:        
        response.set_header('X-Requested-With','XMLHttpRequest')
        response.set_header('Content-Type','application/json')        
        #Session Request hier [False,None,None]        
        if 'atype' in request.query.keys():
            if 'deleteall' == request.query['atype']:
                wx = [None,None]
                for wx[0] in walk(getcwd()+sep+'upload'+sep+cid):
                    for wx[1] in wx[0][2]:
                        unlink(wx[0][0]+sep+wx[1])
                        
                if exists(getcwd()+sep+'upload'+sep+cid):
                    rmdir(getcwd()+sep+'upload'+sep+cid)
                    
                return dumps([True,Application().Tasks(('DataMNG','Set','DeleteAll',cid))])
            
            elif 'deleteItem' == request.query['atype']:
                if request.query['fname'] is not None:
                    if exists(getcwd()+sep+'upload'+sep+cid+sep+request.query['fname']):
                        unlink(getcwd()+sep+'upload'+sep+cid+sep+request.query['fname'])
                    Application().Tasks(('DataMNG','Set','DeleteItem',cid,request.query['fname']))                    
                    return dumps([True,True,request.query['fname']])
            
            else:
                return dumps([True,False,None])            
        
    
@post('/backend/code/<cid>')
def PBackendCode(cid):
    if request.is_xhr:
        response.set_header('X-Requested-With','XMLHttpRequest')
        response.set_header('Content-Type','application/json')                
        #Session Request hier [False,None,None]        
        ftsave = request.files.get('ftsx')
        Application().Tasks(('DataMNG','Set','NewItem',cid,ftsave))        
        if not exists(getcwd()+sep+'upload'+sep+cid):
            if not exists(getcwd()+sep+'upload'):
                mkdir(getcwd()+sep+'upload')
            mkdir(getcwd()+sep+'upload'+sep+cid)
        ftsave.save(getcwd()+sep+'upload'+sep+cid+sep+ftsave.filename)
        return dumps([True,True,ftsave.filename])
        

@post('/login')
def BLogin2():
    if request.is_xhr:
        response.set_header('X-Requested-With','XMLHttpRequest')
        response.set_header('Content-Type','application/json')        
        
        cred = request.forms.getall('credentials')
        
        if not (len(cred[0])==0 or len(cred[1])==0):
            authrs = Application().Tasks(('Users','auth',cred))
            if authrs[0]:
                return dumps([True,Application().Tasks(('Sessions','add',request.remote_addr))])
                #return dumps([False,'Hitten!'])
            
            else:
                return dumps([False,authrs[1]])            
        else:
            return dumps([False,'Please fillout both fields!'])
   
   
@post('/newpass')
def NLogin2():
    if not request.is_xhr:
        cred = request.forms.getall('credentials')
        if len(cred[0])!=0 and len(cred[1])!=0:
            if Application().Tasks(('Users','add',cred))[0]:
                redirect('/login')
            
        else:
            redirect('/login')
    
@get('/<filename>')
def getFileName(filename):
    #if match(ur'^[a-zA-Z0-9]{5,20}\.(pdf|zip|tar\.bz2|7z)$',filename) is not None:
    return getUtility(ITemplate).render('intro.tpl',{})

@post('/<filename>')
def getFileName2(filename):
    #if match(ur'^[a-zA-Z0-9]{5,20}\.(zip|tar\.bz2|7z)$',filename) is not None:
    otpass = request.forms.get('otpass')    
    rsx = Application().Tasks(('DataMNG','Get','DownloadItem',(otpass,filename)))    
    if rsx[0]:        
        return static_file(filename,getcwd()+sep+'upload'+sep+otpass)
    
    else:
        return rsx[1]