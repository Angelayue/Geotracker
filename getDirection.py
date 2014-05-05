""" This google query to convert address to gis info"""

import urllib
import re
import sys
from interface import *

"""
This method format the url request
standard web request
http://maps.googleapis.com/maps/api/directions/json?origin=Toronto
&destination=Montreal
&sensor=false
"""
def urlformator(origin, destination):
	url= "http://maps.googleapis.com/maps/api/directions/json?origin="
	url= url + origin + "&destination=" + destination + "&sensor=false&language=fr-FR&unit=metric"
	return url

	
def gethtml(url):
	page= urllib.urlopen(url)
	html= page.read()
	return html
	
def findgis(html):
	latgroup=re.findall(r"""\blat\"\ :\ [+-]?\d+(?:\.\d+)?""",html,re.X)
	lnggroup=re.findall(r"""\blng\"\ :\ [+-]?\d+(?:\.\d+)?""",html,re.X)
	gis = []
	#print len(latgroup)
	for i in range  (4, len(latgroup),2):
		#distance=re.findall(r"[-+]?\d*\.\d+|\d+",distancegroup[i])
		lat=re.findall(r"[-+]?\d*\.\d+|\d+",latgroup[i])
		lng=re.findall(r"[-+]?\d*\.\d+|\d+",lnggroup[i])	
		gis.append([int(float(lat[0])*10000), int(float(lng[0])*10000)])
	return gis

def getdistance(html):
	distancegroup=re.findall(r"""\btext\"\ :\ \"\d+\,\d""",html,re.X)
	#print distancegroup
	distance=re.findall(r"\d+\,\d",distancegroup[0])
	distance= int(float(distance[0].replace(',','.'))*100)
	return distance


class Direction:
 	def __init__(self, origin, destination):
 		self.origin=origin
 		self.destination=destination	
		self.url=urlformator(self.origin,self.destination)
		self.html=gethtml(self.url)
		self.distance=getdistance(self.html)
		self.gis=findgis(self.html)



if __name__ == "__main__":	
	#x = Direction(OriginGet(),DistinationGet())
	x = Direction("40.6691, -73.9199","Queens")
	print x.distance
	print x.gis[0][0]
	
	