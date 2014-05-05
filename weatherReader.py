class weather:
	f = open('weather.txt', 'r')
	f.readline()
	weather=f.readline()
	
if __name__ == "__main__":	
	x=weather
	print x.weather
	