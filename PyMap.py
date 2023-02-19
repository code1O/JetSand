
"""Python Module for simplify some python libraries functions"""

# -*- coding: utf-8 -*-
# Hello world :)


# ====================================
# language: Spanish-MX, English-USA
# ====================================


from termcolor import colored
import os
from os import path
import psutil
import keyboard as kb
import playsound
import importlib
import pyautogui as pyt
from time import sleep



def checkStatus():
   if True:
      clear = lambda: os.system('cls')
      clear()
      print(colored(f"If this appears it´s because everything is fine, good job :) ", "green"))
      sleep(3)
      clear()

# ======================================================
# PC information (Bytes, processor, frequency & more...)
#=======================================================



class bytes:

   def get_bytes(bytes, suffix="B"):
      factorbytes = 1024
      for unit in ["", "K", "M", "G", "T", "P"]:
         if bytes < factorbytes:
            print(f"Bytes: {bytes: .2f}{unit}{suffix}")
         else:
            print(colored(f"Error bytes non calculated, try again", "red"))
         bytes /= factorbytes

   def get_freq():

      cpufreq = psutil.cpu_freq()

      print(f"max frequency: {cpufreq.max: .2f} MHz")
      print(f"min frequency: {cpufreq.min: .2f} MHz")


# ===================================
# COMMANDS (OS, PATHS & PIP COMMANDS)
# ===================================


class oscom:

   def _init_lib(library):
      libr = (library)
      if os.path.exists:
         print(colored(f"The library {libr} already exists on the system, try again with another library that doesn´t exists", "light_magenta"))
         exit()
      else:
         os.system(f"pip install {libr}")
      return None   
   
   def _init_os(command):
      comando = (command)
      os.system(comando)
      return None
   
   def _init_path(path):
      pth = (path)
      if os.path.exists(pth):
         os.system(pth)
      return None
   
   def _init_remove(path):
      pth = (path)
      if os.path.exists:
         os.remove(pth)
      return None

   def _init_two_commands(self, Command, command2):
      commands = (Command, command2)
      if commands == True:
         oscom._init_os(Command)
         oscom._init_os(command2)
      else:
         print(colored(f"The commands isn´t specified, try again", "red"))
      

# =============================
# DEFINES KEYBOARD PRESS EVENTS 
# =============================




class Keys:

   def holdkey(firstkey, secondkey):
   
      """KEYS ALLOWED: ALT, ALTGR, FN, CMD & SHIFT """

      fkey = (firstkey)
      skey = (secondkey)

      # Windows key: CTRL + ESC

      pyt.keyDown(fkey)
      pyt.keyDown(skey)

   def presskey(Key):

      """Keyboard numbers & words"""

      frstkey = (Key)
      pyt.press(frstkey)
   
   def _2key(Key, Secondkey):

      """Press two keys"""

      firstkey = (Key)
      secondkey = (Secondkey)

      pyt.press(firstkey)
      pyt.press(secondkey)
   
   def _3key(Key, Secondkey, Thirdkey):

      """Press three keys"""

      firstKey = (Key)
      secondkey = (Secondkey)
      thirdkey = (Thirdkey)

      pyt.press(firstKey)
      pyt.press(secondkey)
      pyt.press(thirdkey)
   
   def _4key(Key, Secondkey, Threekey, Fourthkey):

      """It´s enough to make a short phrase"""

      first = (Key)

      second = (Secondkey)

      thirst = (Threekey)

      fourth = (Fourthkey)

      pyt.press(first)

      pyt.press(second)

      pyt.press(thirst)

      pyt.press(fourth)
   
   def _5key(firstKey, secondKey, thirstKey, fourthKey, fiveKey):

      """Makes a middle phrase"""

      w = (firstKey)

      a = (secondKey)

      s = (thirstKey)

      d = (fourthKey)

      e = (fiveKey)

      pyt.press(w)

      pyt.press(a)

      pyt.press(s)

      pyt.press(d)

      pyt.press(e)
   
   def _10key(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10):

      frst5 = (_1, _2, _3, _4, _5)
      scnd5 = (_6, _7, _8, _9, _10)
      Keys._5key(frst5)
      Keys._5key(scnd5)

# =========================================
# Calls to a program or command with a key
# =========================================

class callKeys:

   def winbt(key): #Key that calls to windows button´s function
      keys = (key)
      if kb.is_pressed(keys):
         Keys.holdkey("CTRL", "ESC") #Windows button
         print(f"{keys} pressed")

   def Cmd(key): #Key that calls to CMD
      keys = (key)
      if kb.is_pressed(keys):
         os.system("cmd.exe")
         print(f"{keys} pressed")
   
   def task(key): #Key that calls to taskmgr.exe
      keys = (key)
      if kb.is_pressed(keys):
         os.system("taskmgr.exe")
         print(f"{keys} pressed")
   
   def path(key, path): #Key that open a path
      keys = (key)
      pth = (path)
      if kb.is_pressed(keys):
         if os.path.exists(pth):
            os.system(pth)
            print(f"{keys} pressed")
   
   def sound(key, path): #Key that play sound from a path (.mp4, mp3. wav, etc..)
      keys = (key)
      pth = (path)
      if kb.is_pressed(keys):
         playsound(pth)
         print(f"{keys} pressed")
   
   def _call_explorer(key):
      keys = (key)
      if kb.is_pressed(keys):
         os.system("explorer.exe")
         print(f"{keys} pressed")
   
   def pwrshell(key):
      keys = (key)
      if kb.is_pressed(keys):
         os.system("powershell.exe")
         print(f"{keys} pressed")

class callings:
   def callCmd():
      oscom._init_os("cmd")
   def callTsk():
      oscom._init_os("taskmgr.exe")
   def callCommand(cmnd):
      oscom._init_os(cmnd)
   def callpwrshll():
      oscom._init_os("powershell.exe")
   def callExplorer():
      oscom._init_os("explorer.exe")


MEM=["C:/","D:/","E:/","F:/","G:/"]

class pc:

   def size_mem(memory, suffix="B"):
      """*Size may not be complete at all*"""
      mem = (memory)
      getsize = os.path.getsize(memory)
      for unit in["K", "M", "G", "T"]:
         print(colored(f"The {mem} disk is {getsize}{unit}{suffix} size", "light_yellow"))
         exit()

   def checkfile(file):
      pcfile = (file)
      if os.path.exists(pcfile):
         print(colored(f"Everything good! {pcfile} is there, go back and be cool,", "green"))
         oscom._init_path(pcfile)
   
   def exe_keys():

      if kb.is_pressed("ESC"):
         print(colored(f"Key pressed: ESC", "light_green"))
         oscom._init_os("control.exe")
      elif kb.is_pressed("SUPR"):
         print(colored(f"Key pressed: SUPR", "light_green"))
         oscom._init_os("Explorer.exe")
      elif kb.is_pressed("INS"):
         Keys.holdkey("win", "i")
      elif kb.is_pressed("tab"):
         callings.callTsk()
      elif kb.is_pressed("imppt"):
         oscom._init_path("C:/")

if __name__ == '__main__':
   checkStatus()