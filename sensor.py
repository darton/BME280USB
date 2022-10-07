from tkinter import *
import threading
import serial
from time import sleep

root = Tk()
var = StringVar()
lbl = Label(root, textvariable = var , width=40, height=5, font=('Consolas', 24, 'bold'))
lbl.pack()

serialPort = serial.Serial(port="COM6", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""

while True:
	if serialPort.in_waiting > 0:
		serialString = serialPort.readline()
		try:
			data = serialString.decode("Ascii")
			sleep(1)
			a = data.split(" ")
			t = round(int(a[1])/1000,1)
			h = int(round(int(a[2])/1000,0))
			p = int(round(int(a[3])/1000,0))
			var.set(f'{t}°C {h}% {p}hPa' )
			root.update()
			
		except:
			break
