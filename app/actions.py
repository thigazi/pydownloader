import re
from additional import Singleton
from transaction import commit
from bottle import request
from zope.component import createObject
from transaction import commit
from persistent import Persistent

import base64, M2Crypto,md5
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
        return rsx
    
    def __Sessions(self,param):
        if param[0] == 'check':
            pass
            
        elif param[0] == 'add':
            sessdata = [base64.b64encode(M2Crypto.m2.rand_bytes(20)),str(time()).split('.')[0]]
            if not self.__root.has_key('sessions'):
                self.__root['sessions'] = ddict({sessdata[0]:sessdata[1]})
            
            else:
                self.__root['sessions'][sessdata[0]] = sessdata[1]
            commit()
            
            return sessdata[0]
        
        elif param[0] == 'update':
            #Alle Sessions Ueberpruefen ob
            pass
        
        elif param[0] == 'delete':
            pass
        
        
    def __UserMNG(self,param):        
        if param[0] == 'add':
            hpass = pbkdf2_sha256.encrypt(param[1], rounds=200000, salt_size=16)
        
        elif param[0] == 'update':
            pass
        
        elif param[0] == 'delete':
            pass
        
        elif param[0] == 'auth':
            if self.__root['backend'].has_key(param[1][0]):
                if pbkdf2_sha256.verify(param[1][1], self.__root['backend'][param[1][0]]):
                    return [True,None]
                
                else:
                    return [False,'Falsches Passwort']
                
            else:
                return [False,'Benutzeraccount existiert nicht']
            
    def __DataMNG(self,param):
        if param[0] == 'Get':
            if param[1] == 'ListCodes':
                pass
            
            elif param[1] == 'CodeDetails':
                pass
            
        elif param[0] == 'Set':
            if param[1] == 'NewEntry':
                pass
            
            elif param[1] == 'DeleteEntry':
                pass
            
class Controller(Singleton):
    def __init__(self):
        self.__root = createObject('dbx').root
    
    def checkData(self,param):    
        rsx = None
        if self.__root['dlist'].has_key(param[0]):
            DObj = self.__root['dlist'][param[0]]
            
            if DObj.has_key(param[1]):
                if DObj[param[1]]['maxtry']>0:                     
                    DObj[param[1]]['maxtry']-=1
                    
                    rsx = [True,None]                    
                    commit()
                    
                else:                    
                    rsx = [False,'Maximale Anzahl Downloads aufgebraucht']
                    
            else:
                rsx = [False,'Angeforderte Datei nicht gelistet']
                
        else:
            rsx = [False,'Key Falsch. Bitte korriegieren.']
            
        return rsx
        
    
    def AddRoot(self):
        print self.__root
        
class DataObject(Persistent):
    def __init__(self):
        pass
    
    def __delete__(self):
        pass