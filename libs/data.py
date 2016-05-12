from additional import Singleton
from zope.interface import Interface,implements
from os import getcwd

from ZODB import DB
from ZEO import ClientStorage

class IDBX(Interface):
    pass

class DBX(object):
    implements(IDBX)
    
    def __init__(self):        
        self.__fsx = ClientStorage.ClientStorage(getcwd()+'/dbx/zeosocket')
        self.__dbx = DB(self.__fsx)
        self.__conn = self.__dbx.open()
        self.root = self.__conn.root()