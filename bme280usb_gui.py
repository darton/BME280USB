from tkinter import Tk, StringVar, Label
import serial
from time import sleep
import platform
import sys


root = Tk()
root.title('BME280')
root.geometry("400x50")
var = StringVar()
lbl = Label(root, textvariable = var, font=('Consolas', 24, 'bold'), 
fg="blue")
lbl.pack()

_os = platform.system()

error_msg = "Raspberry Pico is not connected"


if _os == 'Linux':
    try:
        serialPort = serial.Serial(port="/dev/ttyACM0", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    except:
        print(error_msg)
        sys.exit()
elif _os == 'Windows':
    try:
        serialPort = serial.Serial(port="COM6", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    except:
        print(error_msg)
        sys.exit()
elif _os == 'Darwin':
    try:
        serialPort = serial.Serial(port="/dev/cu.usbmodem11301", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    except:
        print(error_msg)
        sys.exit()
else:
    print('Unknown operating system')
    sys.exit()

serialString = ""

while True:
    try:
        if serialPort.in_waiting > 0:
            serialString = serialPort.readline()
            try:
                data = serialString.decode("Ascii")
                sleep(1)
                a = data.split(" ")
                t = round(int(a[1])/1000,1)
                h = int(round(int(a[2])/1000,0))
                p = int(round(int(a[3])/1000,0))
                print(t, h, p)
                var.set(f'{t}°C {h}% {p}hPa' )
                root.update()
            except:
                break
    except:
        print(error_msg)
        sys.exit()
