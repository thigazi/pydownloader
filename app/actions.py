import re
from additional import Singleton
from transaction import commit
from bottle import request
from zope.component import createObject
from transaction import commit
from persistent import Persistent

import base64, md5
from passlib.hash import pbkdf2_sha256
from time import time
from persistent.list import PersistentList as dlist
from persistent.dict import PersistentDict as ddict
from transaction import commit

class Application(Singleton):
    
    def __init__(self):
        self.__root = createObject('dbx').root
    
    def Tasks(self,param):
        rsx = None
        if param[0] in ('Sessions','Users','DataMNG'):
            if param[0] == 'Sessions':
                rsx = self.__Sessions(param[1:])
            
            elif param[0] == 'Users':
                rsx = self.__UserMNG(param[1:])
                
            elif param[0] == 'DataMNG':                
                rsx = self.__DataMNG(param[1:])
                
        return rsx
    
    def __Sessions(self,param):
        tnow = int(time())
        
        if param[0] == 'check':
            pass
            
        elif param[0] == 'add':
            sessdata = [md5.new(request.remote_addr+str(tnow)).hexdigest(),tnow]
            
            if not self.__root.has_key('sessions'):
                self.__root['sessions'] = ddict({sessdata[0]:sessdata[1]})
            
            else:
                self.__root['sessions'][sessdata[0]] = sessdata[1]
            commit()
            
            return sessdata[0]
        
        elif param[0] == 'update':
            #Alle Sessions Ueberpruefen ob
            self.__Sessions(['update',''])
            pass
        
        elif param[0] == 'delete':
            pass
        
        
    def __UserMNG(self,param):
        if param[0] == 'checkExist':
            if not self.__root.has_key('backend'):
                self.__root['backend'] = {'users':ddict()}
                commit()
            
            if not self.__root['backend'].has_key('users'):
                return [False,None]
            
            elif len(self.__root['backend']['users']) == 0:
                return [False,None]
            
            else:
                return [True,None]
        
        elif param[0] == 'add':
            if not self.__root.has_key('backend'):
                self.__root['backend'] = ddict({'users':ddict({param[1][0]:pbkdf2_sha256.encrypt(param[1][1], rounds=200000, salt_size=16)})})
                
            else:
                if len(self.__root['backend']['users']) == 0:
                    self.__root['backend']['users'] = ddict({param[1][0]:pbkdf2_sha256.encrypt(param[1][1], rounds=200000, salt_size=16)})
            commit()
            
            return [True,None]
        
        elif param[0] == 'update':
            pass
        
        elif param[0] == 'delete':
            pass
        
        elif param[0] == 'auth':
            if self.__root['backend']['users'].has_key(param[1][0]):
                if pbkdf2_sha256.verify(param[1][1], self.__root['backend']['users'][param[1][0]]):
                    return [True,None]
                
                else:
                    return [False,'Falsches Passwort']
                
            else:
                return [False,'Benutzeraccount existiert nicht']
            
    def __DataMNG(self,param):
        if param[0] == 'Get':
            if param[1] == 'ListCodes':                
                codes = self.__root['dlist'].keys()
                
                if len(codes)>0:
                    return [True,codes]
                
                else:
                    return [False,None,0]
            
            elif param[1] == 'CodeDetails':
                if self.__root['dlist'].has_key(param[2]):                    
                    return [True,self.__root['dlist'][param[2]]]
                else:                    
                    return [False,None]
                
            elif param[1] == 'DownloadItem':
                if self.__root['dlist'].has_key(param[2][0]):
                    dentry = self.__root['dlist'][param[2][0]]
                    
                    if dentry.has_key(param[2][1]):
                        if dentry[param[2][1]]['maxtry']==0:
                            return [False,'Alle Downloads aufgebraucht']
                        
                        else:                            
                            dentry[param[2][1]]['maxtry']-=1
                            commit()
                            
                            return [True,None]
                        
                    
                    else:
                        return [False,'Not available']
                        
                
                else:                    
                    return [False,'Not available']
                    
            
        elif param[0] == 'Set':
            if param[1] == 'NewEntry':
                mk = md5.new()
                mk.update(str(time()))                
                if not self.__root.has_key('dlist'):
                    self.__root['dlist'] = ddict()                    
                self.__root['dlist'][mk.hexdigest()[:10]] = ddict()                
                commit()
                
                return mk.hexdigest()[:10]
            
            elif param[1] == 'DeleteAll':                                
                del self.__root['dlist'][param[2]]
                commit()
                return True
                
            elif param[1] == 'NewItem':
                '''
                for xlist in ('flist','dlist'):
                    if not self.__root.has_key(xlist):
                        self.__root[xlist] = ddict()
                        self.__root[xlist][param[2]] = ddict()                
                        '''
                if not self.__root.has_key('dlist'):
                    self.__root['dlist'] = ddict()
                    self.__root['dlist'][param[2]] = ddict()

                self.__root['dlist'][param[2]][param[3].filename] = ddict({'maxtry':3})
                #self.__root['flist'][param[2]][param[3].filename] = pickle.dumps(param[3],protocol=2)                
                commit()
                
            elif param[1] == 'DeleteItem':
                '''for xlist in ('flist','dlist'):
                    if self.__root[xlist][param[2]].has_key(param[3]):
                        del self.__root[xlist][param[2]][param[3]]
                commit()                
                '''
                
                if self.__root['dlist'][param[2]].has_key(param[3]):
                    del self.__root['dlist'][param[2]][param[3]]                    
                commit()
                return True
        
class DataObject(Persistent):
    def __init__(self):
        self.filename = None
        self.fcontent = None
    
    def __delete__(self):
        pass