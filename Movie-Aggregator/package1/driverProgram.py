'''
Created on Mar 4, 2017
@author: Arvind
'''

import sys
from package1.findplugins import findplugins
from package1.formatfactory import formatfactory

if __name__ == '__main__':
    
    Movie  = {};
    save='./Result'   # Save location 
    
    Movie['name']       = str(raw_input("Movie name: "))
    Movie['time']        = str(raw_input("Run time: "))
    Movie['language']   = str(raw_input("Language: "))
    Movie['act']        = str(raw_input("Lead actor: "))
    Movie['genre']      = str(raw_input("Genre: "))
    #print(Movie)
    try:
        pluginclass = findplugins("./Plugins",formatfactory)        # we get the reference of the class
    except Exception:
        print "is the plugin directory changed?"
        sys.exit()
    try:    
        d = pluginclass()        # We're instantiating the selected Plugin in runtime    
        #print type(d)
    except Exception:                               # The plugin can't be instantiated.
            print"Problem with the plugin, try another format."
            sys.exit()
                
    try:
        d._write(Movie,save)
        print("saved. :)")
    except Exception:
        print "Oops. Is the document instance open in any application? If not, check the save location. Something awful happened."