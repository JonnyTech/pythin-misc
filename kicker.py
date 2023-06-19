#pip3 install pyserial
from tkinter import *
import tkinter as tk
import serial
import time

root=Tk()
root.title('WIM Kicker Test')
ser=serial.Serial()

def ReadSerialPortLoop():
  while ser.is_open:
    serIn=ser.read()
    if len(serIn)==0:
      break
    textbox.insert('end',serIn)
  root.after(1,ReadSerialPortLoop)

def serialConnect():
  ser.port=inpPort.get()
  ser.baudrate="9600"
  ser.parity=serial.PARITY_NONE
  ser.stopbits=serial.STOPBITS_ONE
  ser.bytesize=serial.EIGHTBITS
  ser.timeout=1
  ser.open()
  ser.flush()
  if ser.is_open:
    buttonConnect["state"]=DISABLED
    buttonOpenArm["state"]=NORMAL

def sendArmOpen():
  ser.write(b"A")

inpPort=Entry()
inpPort.insert(END,'serial-port')
inpPort.select_range(0,tk.END)
inpPort.focus_set()
inpPort.grid(row=0,column=0)

inpBaud=Entry()
inpBaud.insert(END,'115200')
inpBaud.grid(row=1,column=0)

buttonConnect=Button(root,text="Connect",command=serialConnect)
buttonConnect.grid(row=2,column=0)

buttonOpenArm=Button(root,text="Open Arm",command=sendArmOpen)
buttonOpenArm.grid(row=3,column=0)
buttonOpenArm["state"]=DISABLED

textbox=Text(root,height=12,width=40)
textbox.grid(row=4,column=0)

root.geometry("350x350")
root.after(1,ReadSerialPortLoop)
root.mainloop()
