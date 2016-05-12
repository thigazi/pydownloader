from re import match
from os import getcwd
from bottle import static_file
from zope.component import getUtility
from libs.output import ITemplate
from actions import Controller,Application
from bottle import route,static_file,request,response,get,post,error
from json import dumps

@get('/js/<filename>')
def JSFiles(filename):
    return static_file(filename,getcwd()+'/static/js')

@get('/img/<filename>')
def IMGFiles(filename):
    return static_file(filename,getcwd()+'/static/img')

@get('/')
def Teste():
    Controller().AddRoot()

@get('/login')
def BLogin():
    if not request.is_xhr:
        return getUtility(ITemplate).render('login.tpl',{'eflag':False,'emsg':None})

@get('/backend')
def BackendG():
    if not request.is_xhr:
        codes = Application().Tasks(('DataMNG','Get','ListCodes'))
        return getUtility(ITemplate).render('backend.tpl',{'codes':Application().Tasks(('DataMNG','Get','ListCodes')),'cid':[False,None]})

@post('/backend')
def BackendP():        
    if request.is_xhr:
        pass

@get('/backend/code/<cid>')
def GBackendCode(cid):
    if not request.is_xhr:
        dinfo = Application().Tasks(('DataMNG','Get','CodeDetails',cid))[1]        
        
        #Session JA
        return getUtility(ITemplate).render('backend.item.tpl',{
            'codes':Application().Tasks(('DataMNG','Get','ListCodes')),
            'cid':[True,cid],
            'dinfo':[dinfo.keys(),dinfo]
        })
    
        
@post('/backend/code/<cid>')
def PBackendCode(cid):
    if request.is_xhr:
        pass


@post('/login')
def BLogin2():
    if request.is_xhr:
        response.set_header('X-Requested-With','XMLHttpRequest')
        response.set_header('Content-Type','application/json')        
        
        cred = request.forms.getall('credentials')
        if len(cred) == 2:
            authrs = Application().Tasks(('Users','auth',cred))
            if authrs[0]:
                return dumps([True,Application().Tasks(('Sessions','add'))])
            
            else:
                return dumps([False,authrs[1]])                
            
        else:
            return dumps([False,'Bitte beide Felder ausf&uuml;llen'])
        

@get('/<filename>')
def getFileName(filename):
    if match(ur'^[a-zA-Z0-9]{5,20}\.(zip|tar\.bz2|7z)$',filename) is not None:
        return getUtility(ITemplate).render('intro.tpl',{})

@post('/<filename>')
def getFileName2(filename):
    if match(ur'^[a-zA-Z0-9]{5,20}\.(zip|tar\.bz2|7z)$',filename) is not None:
        otpass = request.forms.get('otpass')        
        rsx = Controller().checkData((otpass,filename))
        
        if rsx[0]:
            return static_file(filename,getcwd()+'/static')
        
        else:
            return rsx[1]