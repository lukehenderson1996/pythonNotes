Python Notes written by Luke Henderson

Required imports:
pip install pillow

Recomended:
pip install numpy

How????
pip install win32gui
pip install pywintypes

Table of contents:
    pics: gui documentation info, gui icons can be stored here, etc
    .gitignore: tells git to ignore datalogs and compiled python files
    readme.txt
    scripts:
        archive: outdated/deprecated code or reference material
        formatting: standard formatting advice and templates for Luke's projects
        testBenches: unfinished testbench suite
        run scripts.bat: batch file that opens a clean command prompt to run python with
        shortTest.py: template to help with quick debugging if needed

        colors.py: print to cmd line in color
        debugTools.py: look into objects and data structures
        gui: simple threaded gui with easy API
        logger.py: logging wrapper for scientific style saving of results to disk
        plot.py: seaborn (matplotlib) wrapper with easy API
        utils.py: various assorted macros and utilities
            



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


