
"""

JetSand is an programming language based on python written with python

Twitter - https://www.twitter.com/@Jthe_Dais/


"""

from termcolor import colored 
from PyMap import *
from PyMap import oscom as osc
import os
from os import path
import webbrowser as wb
import datetime
from datetime import date


def __Sys_write__(text:str|float|int):

    """Prints an string, int or float like python print function"""

    if type (text) == str:
        print(str(text))
    elif type (text) == int:
        print(int(text))
    elif type (text) == float:
        print(float(text))

def __getwrite__(text:str|int|float):

    """
    
    Works like the python input function
    
    It prints the input data 

    """

    if type (text) == str:
        geting = input(str(text))
        print(f"output: {geting}")
        
def __int_input__(text:str, color:str):
    """int from an input function"""
    
    int(input(colored(f"{text}", color)))

def __float_input__(text:str):
    """float from an input function"""
    
    float(input(text))

def __power__(number:int|float, pot:int|float):

    """
    
    x^n

    
    for example: 4^2 that´s 16

    """

    el = (pot)
    num = (number)
    if type(number) == int:
        elev = num**el or num^el
    elif type(number) == float:
        elev = num**el or num^el
    print(colored(f"{number}^{pot} = {elev}", "yellow"))

def __pawer_input__(color:str, text:str, numpower:int|float):
    put = int(input(colored(text, color)))
    get = put ** numpower
    __Sys_write__(colored(f"{put}^{numpower} = {get}", "light_yellow"))
    
def __verify__(status=None):

    """Verify if the code is working"""

    if status == "__main__":
        print(colored(f"Hello world!", "light_green"))

# def a list of strings, float & ints
def __list__(list:str|int):

    """Prints the elements from the list"""

    for i in range(len(list)):
        __Sys_write__(list[i])
    
#def a tuple of strings, float & ints
def __tuple__(tuple:list|int):

    """Prints the elements from the tuple"""

    for i in range(len(tuple)):
        __Sys_write__(tuple[i])

def __link__(link:str):
    lnk = (link)
    link1 = "https://www."+lnk+".com/"
    print(colored(f"{link1} is a link to {str(lnk)} site", "light_green"))
    wb.open(link1)


class dirs:
    
    def __remove_c__(User:str, path:str):
        """
        Remove files from C:/ path
        
        """

        pathdir = "C:/Users/" + User + "/OneDrive/Escritorio/" + path
        os.remove(pathdir)
        
    def __remove_usb__(User:str, path:str):
        """
        Remove files from USB path

        D:/path

        """

        pathdir = User + ":/" + path
        os.remove(pathdir)
    
    def __remove__cfold__(User:str, path:str, file:str):
        """
        Remove folder content from Desktop

        """

        pathComplete = "C:/Users/" + User + "/OneDrive/Escritorio/" + path + "/" + file
        os.remove(pathComplete)
        
    def __remove_usfold__(path:str, file:str):
        """
        Remove folder contents from USB

        D:/path/file

        """

        pathdir = "D:/" + path + "/" + file
        os.remove(pathdir)
        
    # def a link to path
    
    def __link_to_path__(User:str, link:str):
        lnk = (link)
        link1 = "C:/Users/" +  User + "/OneDrive/Escritorio/" + lnk #Windows 11
        oscom._init_path(link1)

    # print the files from a path

    def __print_files__(path:str):
        if os.path.exists(path):
            print(colored(f"{path} path exists", "light_green"))
            for root, files in os.walk(path):
                for file in files:
                    print(os.path.join(root, file))
        else:
            print(colored(f"{path} doesn´t exists, try again with another path", "light_red"))

    def __print_paths__(User:str, path:str):

        paths = (path)

        linkC = "C:/Users/" + User + "/" + "OneDrive/Escritorio/" + paths 
        linkUsb = User + "" # D:/, E:/, F:/, G:/, etc...
        for i in (linkC, linkUsb):
            if os.path.exists(i):
                for root, files in os.walk(i):
                    for file in files:
                        print(colored(os.path.join(root, file), "light_magenta"))
    
    def __open_path__(User:str, path:str):
        
        linkC = "C:/Users/" + User + "/OneDrive/Escritorio/" + path
        osc._init_path(linkC)