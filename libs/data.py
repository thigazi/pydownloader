from additional import Singleton
from zope.interface import Interface,implements
from platform import system

from ZODB import DB
from ZEO import ClientStorage

class IDBX(Interface):
    pass

class DBX(object):
    implements(IDBX)
    
    def __init__(self):
        if system() == 'Linux':
            self.__fsx = ClientStorage.ClientStorage(getcwd()+'/dbx/zeosocket')
            
        elif system() == 'Windows':
            self.__fsx = ClientStorage.ClientStorage(('127.0.0.1',3000))
            
        self.__dbx = DB(self.__fsx)
        self.__conn = self.__dbx.open()
        self.root = self.__conn.root()
        
        
    def __delete__(self):
        self.__conn.close()
        self.__dbx.close()
        
        del self.root
        del self.__dbx
        del self.__conn
        del self.__fsx