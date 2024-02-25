Python Notes written by Luke Henderson

Required imports:
pip install pillow

Recomended:
pip install numpy

How????
pip install win32gui
pip install pywintypes


BUGS:
general
    use type checking/click lower right hand corer {} to turn it on in a .py file
        see if -> int makes a difference now
logger
    cannot accept None as input data for csv file, maybe other datatypes
    cannot accept 'bytes' datatype
gui
    cannot handle main thread using input(), or ut.pause()
    queue consumer needs to be updated to first in first out

to do:
general:
learn pickle
gui:
    '''for sendkeys: need error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for 
    Visual Studio": https://visualstudio.microsoft.com/downloads/'''
    # from SendKeys import SendKeys
    # SendKeys('%{TAB}') # to alt tab back to he cmd window

Periodic code audit:
    verify each function never assigns to an inputted object without object.copy(), unless that's the intent.

Table of contents:
pythonNotes git repo
    datalogs: data logs stored here
    .gitignore: tells git to ignore datalogs and compiled python files
    code-workspace: for VS code
    readme.txt
    scripts:
        custom modules to help:
            logger help: contains formatting templates for datalogs
            colors.py: print to cmd line in color
            debugTools.py: look into objects and data structures
            gui: not finished
        logger help (folder)
            contains templates for datalogging
        formatting help:
            formatting.py: Luke's formatting for a main python file
            formattingModule: Luke's formatting for a sub python file (module)
        tutorial.py: simple examples
        test modules for advanced examples
            test_[module name]
        
