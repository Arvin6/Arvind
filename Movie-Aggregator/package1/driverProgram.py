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
        listofplugins = findplugins("./Plugins",formatfactory)
    except Exception:
        print "is the plugin directory changed?"
        sys.exit()
        
    i=1
    
    for eachplugin in listofplugins:
        print i,(eachplugin.__doc__).strip("\n")
        i+=1    
        
    k=int(input('Select one format to save..'))
    
    try:    
        d = listofplugins[k-1]()        # We're instantiating the selected Plugin in runtime    
        #print type(d)
    except Exception:
        if k<1 or k>len(listofplugins):             # Invalid choice, Nope!
            print "Invalid choice, exiting"
            sys.exit()
        else:                                       # The plugin can't be instantiated.
            print"Problem with the plugin, try another format."
            sys.exit()
                
    try:
        d._write(Movie,save)
        print("saved. :)")
    except Exception:
        print "Oops. Did you close the opened document instance? If not, check the save location .Something awful happened."