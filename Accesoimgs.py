# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:46:07 2020

Copyright 2020 Javier A. Cuartas Micieces

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
import tkinter as tk
from tkinter import Tk
import json
import time, datetime
import os
import copy
    
class TkWindow:
    def __init__(self,*args,**kwargs):
        self.cp=args[0]
        
    def error_f(self,filename):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title('Error de reconocimiento de icono')
        msg=tk.Message(self.root,text="Por favor, capture con Recortes de Windows u otro programa similar la imagen de "+filename+" y guárdelo en una carpeta de Accesoimgs, si hay una nueva alternativa de imagen en el mismo nivel que esta, cree una carpeta Accesoimgsn donde n sea un nuevo número distinto de los de las carpetas existentes.",width=500)
        msg.grid(padx=0,pady=0)
        self.root.mainloop()
        
    def error_importing(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title('Error de importación')
        msg=tk.Message(self.root,text="Por favor, instale las librerías de python pyautogui y keyboard, para que el script pueda funcionar correctamente.",width=500)
        msg.grid(padx=0,pady=0)
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
                
class MainWindow:
    def __init__(self,openft):
        self.cp = str.replace(self.f.__code__.co_filename,"\\","\\\\")[:-17]
        self.br=TkWindow(self.cp)
        pa.FAILSAFE=True
        with open(self.cp+"inputs.json") as f:
            self.inputdict=json.load(f)
        for keysr in self.inputdict.keys():
            if self.inputdict[keysr]["activated"][0]==str(1):
                nametime=datetime.datetime.now().strftime("_%d-%m-%Y_%H-%M")
                self.run_clicksroute(keysr,nametime,openft)

    def run_clicksroute(self,routine,nametime,openft):
        if openft==1:
            x0,y0=self.openf(routine)
        else:
            x0,y0=pa.size()
        iinps=0
        for sv,kv in enumerate(self.inputdict[routine]["clicksroute"]):
            if kv[0]==str(0):
                for el in kv[2]:
                    if el[1]==str(1):
                        pa.keyDown(el[0])
                    elif el[1]==str(0):
                        pa.keyUp(el[0])
                    time.sleep(float(kv[3]))
            else:
                err_m=self.try_imgs(kv[0],kv[2],kv[3],kv[4],1,kv[5])
                if err_m==1:
                    break
            if kv[1]==str(1):
                if self.inputdict[routine]["inputs"][iinps][1]==":":
                    pa.write(self.inputdict[routine]["inputs"][iinps]+routine+nametime+self.inputdict[routine]["outputformat"][0])
                else:
                    pa.write(self.inputdict[routine]["inputs"][iinps])
                iinps=iinps+1
            try:
                pa.moveTo(x=x0-80,y=y0-4)
                if self.inputdict[routine]["clicksroute"][sv+1][0]!=str(0):
                    g=1
                    time0=datetime.datetime.now()
                    timeerror=time0+datetime.timedelta(minutes=5)
                    while (time0<timeerror and g==1):
                        time0=datetime.datetime.now()
                        g=self.try_imgs(self.inputdict[routine]["clicksroute"][sv+1][0],self.inputdict[routine]["clicksroute"][sv+1][2],self.inputdict[routine]["clicksroute"][sv+1][3],self.inputdict[routine]["clicksroute"][sv+1][4],None,self.inputdict[routine]["clicksroute"][sv+1][5])
                        time.sleep(1)
            except:
                pass
        pa.moveTo(x=x0-80,y=y0-4)

    def clickinput(self,filename,clicksnumber,delay,positioner):
        clicksnumber=int(clicksnumber)
        p0=int(positioner[0])
        p1=int(positioner[1])
        delay=float(delay)
        try:
            x1,y1=pa.locateCenterOnScreen(self.cp+filename)
            pa.click(clicks=clicksnumber,x=x1+p0,y=y1+p1)
            time.sleep(delay)
            return 0
        except:
            return 1
        
    def openf(self,routine):
        x0,y0=pa.size()
        pa.click(x=x0,y=y0-4)
        pa.moveTo(x=x0-80,y=y0-4)
        return x0,y0
    
    def check_image(self,g,imagename):
        try:
            xc,yc=pa.locateCenterOnScreen(self.cp+imagename)
            g=True
        except:
            g=None
        return g

    def try_imgs(self,filename,clicksnumber,delay,positioner,checkorclick,skipable):
        h=[el for el in os.listdir(self.cp[:-2]) if all([el.startswith("Accesoimgs")==True,el.endswith(".py")!=True])]
        h.reverse()
        origcp=copy.copy(self.cp)
        rootcp=copy.copy(self.cp)
        i=len(h)-1
        err_c=0
        while i!=-1:
            self.cp=rootcp+h[i]+"\\\\"
            if checkorclick==None:
                err_m=1 if self.check_image(checkorclick,filename)==None else 0
                err_c=1
            else:
                err_m=self.clickinput(filename,clicksnumber,delay,positioner)
            if err_m!=1:
                err_m=0
                break
            else:
                i=i-1
        if err_m==1 and err_c!=1:
            if skipable=="1":
                print(filename)
                print("skip")
                pass
            else:
                self.br.error_f(filename)
        self.cp=origcp
        return err_m

    def f(self): pass


try:
    import pyautogui as pa
except:
    tr=TkWindow("").error_importing()

if __name__=="__main__":
    app=MainWindow(1)

