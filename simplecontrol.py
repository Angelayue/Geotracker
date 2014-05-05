import serial
from serial.tools import list_ports

print(list(serial.tools.list_ports.comports()))


ser = serial.Serial('/dev/cu.usbmodemfd121')
print ser.name 

terminate=1 #0/1 teminate/ continue
while (terminate):
	inputTest=input('Enter your command: ')
	
	if input!= "exit":
		ser.write(inputTest)
		line=ser.readline()
		print line
	else :
		terminate=0
