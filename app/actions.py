import re
from .additional import Singleton
from transaction import commit
from bottle import request
from zope.component import createObject
from transaction import commit
from persistent import Persistent

from hashlib import md5
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
        
        if param[0] == 'checkExpired':
            rs = None
            sakeys = self.__root['backend']['sessions'].keys()
            if param[1] in self.__root['backend']['sessions']:                                
                tdiff = tnow-self.__root['backend']['sessions'][param[1]]
                if tdiff>300:
                    rs = [False,None]
                    del self.__root['backend']['sessions'][param[1]]
                    sakeys = self.__root['backend']['sessions'].keys()
                    commit()
                    
                else:
                    self.__root['backend']['sessions'][param[1]] = tnow
                    
                    rs = [True,None]
            
            else:
                rs = [False,None]
            
            for sk in sakeys:                
                tdiff = tnow-self.__root['backend']['sessions'][sk]
                if tdiff>300:
                    del self.__root['backend']['sessions'][sk]
                    
            commit()
            return rs
            
        elif param[0] == 'add':            
            dg = md5()
            dg.update(bytes(request.remote_addr+str(tnow),encoding='utf8'))
            sessdata = [dg.hexdigest(),tnow]
            
            if 'sessions' not in self.__root['backend']:
                self.__root['backend']['sessions'] = ddict({sessdata[0]:sessdata[1]})
            
            else:
                self.__root['backend']['sessions'][sessdata[0]] = sessdata[1]
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
            if 'backend' not in self.__root:
                return [False,None]
            
            if 'users' not in self.__root['backend']:
                return [False,None]
            
            elif len(self.__root['backend']['users']) == 0:
                return [False,None]
            
            else:
                return [True,None]
        
        elif param[0] == 'add':
            if 'backend' not in self.__root:
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
            if param[1][0] in self.__root['backend']['users']:
                if pbkdf2_sha256.verify(param[1][1], self.__root['backend']['users'][param[1][0]]):
                    return [True,None]
                
                else:
                    return [False,'wrong password']
                
            else:
                return [False,'user account does not exist']
            
    def __DataMNG(self,param):
        if param[0] == 'Get':
            if param[1] == 'ListCodes':
                if 'dlist' not in self.__root:
                    self.__root['dlist'] = ddict()
                    commit()
                    
                codes = self.__root['dlist'].keys()
                
                if len(codes)>0:
                    return [True,codes]
                
                else:
                    return [False,None,0]
            
            elif param[1] == 'CodeDetails':
                if param[2] in self.__root['dlist']:
                    return [True,self.__root['dlist'][param[2]]]
                else:                    
                    return [False,None]
                
            elif param[1] == 'DownloadItem':
                if param[2][0] in self.__root['dlist']:
                    dentry = self.__root['dlist'][param[2][0]]
                    
                    if param[2][1] in dentry:
                        if dentry[param[2][1]]['maxtry']==0:
                            return [False,'Alle downloads depleted']
                        
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
                mk = md5()
                mk.update(str(time()).encode('utf8'))
                if 'dlist' not in self.__root:
                    self.__root['dlist'] = ddict()                    
                self.__root['dlist'][mk.hexdigest()[:10]] = ddict()                
                commit()
                
                return mk.hexdigest()[:10]
            
            elif param[1] == 'DeleteAll':                                
                del self.__root['dlist'][param[2]]
                commit()
                return True
                
            elif param[1] == 'NewItem':
                if 'dlist' not in self.__root:
                    self.__root['dlist'] = ddict()
                    self.__root['dlist'][param[2]] = ddict()

                self.__root['dlist'][param[2]][param[3].filename] = ddict({'maxtry':3})
                commit()
                
            elif param[1] == 'DeleteItem':
                if param[3] in self.__root['dlist'][param[2]]:
                    del self.__root['dlist'][param[2]][param[3]]                    
                commit()
                return True
        
class DataObject(Persistent):
    def __init__(self):
        self.filename = None
        self.fcontent = None
    
    def __delete__(self):
        pass