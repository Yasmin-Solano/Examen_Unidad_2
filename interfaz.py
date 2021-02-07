# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:53:55 2020

@author: Yasmin
"""

import psycopg2
import serial
from tkinter import *
import time
from insert import insert_TEMPERATURE




class BaseDatos:
    def __init__(self,hora_1,temp):
        
        self.hora_1 = hora_1
        self.temp = temp # Arduino.readline()
        
        insert_TEMPERATURE(hora_1, temp)
        print("SE GURADRON LOS DATOS CORRECTAMENTE")
        
class Serial():
    def build(self):
        return BaseDatos()

if __name__ == '__main__':
    try:
        Arduino = serial.Serial("COM8",9600, timeout=0.25)
    except Exception as e:
        print ("Error al conectar")
        print(e)
       
        
asd= BaseDatos(time.strftime("%I:%M:%S"),Arduino.readline().decode("UTF-8"))  
    
BinSalir = True;       


def Lectura():
    global BinSalir
    
    while BinSalir:
        temp=Arduino.readline() 
        print(temp)
        print("DatoCorrecto")
        temperatura.set(temp)
        try:
            root.update()
        except TclError:
            Salir()
            print("TK Cerrado")
        

def Salir():
    global BinSalir 
    BinSalir = False;
    try:
        root.quit()
        root.destroy()
    except:
        pass
    Arduino.close()
        
root = Tk()

temperatura = StringVar()
root.title("PROGRAMACIÓN II")
root.geometry("400x300")
root.iconbitmap("./Imagen/UNT_LOGO.png.ICO")


imageCerrar = PhotoImage(file="./Imagen/Bot_Cerrar.png")


Portada = PhotoImage(file = "./Imagen/hidroponia.png") 
background_label = Label(root, image=Portada) 
background_label.place(x=0, y=0) 


labeltitulo = Label(root,text="TEMPERATURA(°C)",font=("Arial Black",11), fg = "green")
labeltitulo.grid(row=0,column=1,padx=20,pady=30)



labeltemp = Entry(root,textvariable=temperatura, width=5, font=("Arial Black",11), fg = "green" )
labeltemp.grid(row=0,column=3,padx=10,pady=20)


B_Salir = Button(root, image=imageCerrar,width=50, height=50, font=("Arial Black",11), command=Salir)
B_Salir.place(x=340,y=240)


Lectura() 
root.mainloop()

Arduino.close()  



