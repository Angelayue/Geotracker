""" Connect to arduino """

import serial
from interface import *
from getDirection import *

class arduino:
	ser = serial.Serial('/dev/cu.usbserial-A602TP60')
	"""
	This one get gis from broad
	"""
	ser.write("g")
	line=ser.readline()
	print line


	#x = Direction(OriginGet(),DistinationGet())
	#x = Direction("Brooklyn","Queens")
	
	#write distance to arduino
#	ser.write(x.distance)
	"""
	#write gis to arduino
	for i in range (1, len(x.gis)):
		print x.gis[i]
#		ser.write(x.gis[i])
		pass
	
	line = ser.readline()
	print line	
"""

if __name__ == "__main__":	
	y = arduino()	
