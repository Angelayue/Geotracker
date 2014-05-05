""" This google query to convert address to gis info"""

import urllib
import re
import sys
from interface import *

def urlformator(address):
		url= "https://maps.googleapis.com/maps/api/geocode/json?address="
		url= url + address + "&sensor=true"
		return url
	
def gethtml(url):
		page= urllib.urlopen(url)
		html= page.read()
		return html
	
def findlat(html):
		latgroup=re.findall(r"""\blat\"\ :\ [+-]?\d+(?:\.\d+)?""",html,re.X)
		lat=re.findall(r"[-+]?\d*\.\d+|\d+",latgroup[0])
		lat=float(lat[0])
		return lat

def findlng(html):
	lnggroup=re.findall(r"""\blng\"\ :\ [+-]?\d+(?:\.\d+)?""",html,re.X)
	lng=re.findall(r"[-+]?\d*\.\d+|\d+",lnggroup[0])
	lng=float(lng[0])
	return lng


class googleQuery:
 	def __init__(self, address):
 		self.address=address	
		self.url=urlformator(self.address)
		self.html=gethtml(self.url)
		self.lat=findlat(self.html)
		self.lng=findlng(self.html)



if __name__ == "__main__":	
	x=googleQuery(AddressGet())
	print x.lat
	print x.lng
	
	