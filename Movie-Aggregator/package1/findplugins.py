'''
Created on Mar 4, 2017
This module searches for any new modules in the Plugins folder at runtime.
@author: Arvind
'''
import os
from package1.formatfactory import formatfactory

def findplugins(path,classtype):
    plugins=[]
    
    for root,dirs,files in os.walk(path):
        for fileeach in files:
            if fileeach.endswith(".py"):
                mod = path[2:]+"."+fileeach[:-3]            # We're making it import-able by concatenating Plugin.modulename, this will need change if we change the Plugin directory
                #print(mod)
                module = __import__(mod)
                #print type(module)
                d = module.__dict__
                #print(d)
                for m in mod.split('.')[1:]:
                    d = d[m].__dict__
            
                for key, entry in d.items():
                    if key == classtype.__name__:
                        continue
                    try:
                        if issubclass(entry, classtype):
                            #print("Found subclass: "+key)
                            plugins.append(entry)
                    except TypeError:
                        pass  
    i=1
    for eachplugin in plugins:
        print i,(eachplugin.__doc__).strip("\n")
        i+=1    
    k=int(input('Select one format to save.. '))   
    while (k<1 or k>len(plugins)):
        k=int(input('Invlaid, enter again.. '))
                        
    return plugins[k-1]     # A reference to the class is returned.

'''
For testing
'''
if __name__ == '__main__':
    pluginsclass = findplugins('./Plugins',formatfactory)          # Explicitly addressed the plugins folder in the project.
    print(pluginsclass().__class__)