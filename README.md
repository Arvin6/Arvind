# Arvind
This is the repository for Movie-Aggregator assignment from Multunus. Check out. (Reflection)
[CLI based Movie aggregator]

There are three plugins with the app.
1. Docx
2. PDF
3. Plaintext

The Application finds and displays all available plugins and lets the user choose which format they want to use in runtime.
No change to the code needed, when adding a new plugin(format to save).
However, the new plugin has to follow certain guidelines for seamless integration with the app.

# Guidelines for adding new plugin

1 -> The Plugin should be added to the ./Plugins folder in package1.

2 -> The Plugin should have a docstring ( __DOC__ ) in it's class which says "Save as XXX" where XXX is the format. 
      Eg - "Save as pdf"
      
3 -> The Plugin should inherit the formatfactory class in package1, and have it's implementation of "_write(self,somedict,saveloc)" method.     (Check the source)

# To run this app,

You can clone/download the project and run on eclipse.

-> Find the driverProgram.py and run. (Everything will run as is.)

# Folders
./Result/  -> This is the folder for output by default. If you want to change that, change it in driverProgram.py.
./Plugins/ -> This is where your new plugins exist.

# Modules and Description 

driverProgram.py -> The main driver module.

findplugins.py -> This module searches all python modules in the "./Plugins/" folder that extends the formatfactory class and returns the necessary reference for instantiation during runtime. (If your plugin doesn't extend the formatfactory class, it may not be listed)  (Check source)

formatfactory.py -> Base class for plugins. [check source]

docxmodule.py | pdfmodule.py | plaintextmodule.py -> Plugins for each format.

# All modules can be run and tested seperately. [Check Source.]

