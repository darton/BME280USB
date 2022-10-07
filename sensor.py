from tkinter import Tk, StringVar, Label
import threading
import serial
from time import sleep

root = Tk()
root.title('BME280')
root.geometry("400x50")
var = StringVar()
lbl = Label(root, textvariable = var, font=('Consolas', 24, 'bold'), fg="blue")
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
