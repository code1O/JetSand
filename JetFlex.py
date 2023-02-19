
# Enough Modules for work
from JetSand import __Sys_write__, __getwrite__, __power__, __verify__, __list__, __tuple__
from JetSand import __link__, __link_to_path__, __print_files__, __print_paths__, dirs
from termcolor import *

#=====================================================


wr = __Sys_write__              # print function
gw = __getwrite__               # input function
pau = __power__                 # power function
diany = __verify__              # verify function
may = __list__                  # list function
jet = __tuple__                 # tuple function
links = __link__                # links with https domain
lex = True                      # lexer (True)
notlex = False                  # not lexer (False)
pathlink = __link_to_path__     # link to path function
listfiles = __print_files__     # print files function 
paths = __print_paths__         # print any path including USB paths
c = dirs                        # pc directories class
rg = range                      # range function
r = str                         # string function
it = int                        # int function
fl = float                      # float function
dct = dict                      # dict function
rc = c.__remove_c__             # remove C:/ files
rmusb = c.__remove_usb__        # remove USB files
rdfold = c.__remove__cfold__    # Remove any folder content from desktop
rufold = c.__remove_usfold__    # Remove any folder content from USB


#=====================================================


# Libraries for maths or scientific reasons


from math import *
from matplotlib import *
from scipy import *
from astropy import *
from wolframalpha import *


# Libraries for other uses 


from webbrowser import *
from pyttsx3 import * 
from tkinter import *
from tkinter import messagebox as mgbx
from speech_recognition import *
from pynput import *
from keyboard import *
from pyautogui import *