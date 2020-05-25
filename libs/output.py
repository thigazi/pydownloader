from .additional import Singleton
from os import getcwd
from jinja2 import Environment, FileSystemLoader
from zope.interface import Interface,implementer,Attribute


class ITemplate(Interface):
    pass

@implementer(ITemplate)
class Template(object):
    
    def __init__(self):        
        self.__env = Environment(loader=FileSystemLoader(getcwd()+'/tpl'),cache_size=0)
        
    def render(self,name,param):
        return self.__env.get_template(name).render(**param)