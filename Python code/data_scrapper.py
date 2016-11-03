# Web Scrapper 
# Import Libraries to access and retrieve data from HTML and XML files

import requests 
from BeautifulSoup import BeautifulSoup
import csv
import os

homepage = "http://www.census.gov" # United States Census Bureau

def getHTML(url):
	response = requests.get(url)
	htmlOutput =  BeautifulSoup(response.content)
	return htmlOutput

#Extracting Layout of the File template
def fileTemplate(htmlOutput):
	template = str(htmlOutput.find('a',attrs={'title': 'File layout'}))[9:73]
	template = homepage + template
	data = getHTML(template)
	print data
	header = ['Year','FIPS_state_code','FIPS_county_code','Age_group','Race-Sex','Ethnic_origin','population']
	dataWriter(data,"data_1990_1999_template.txt")
	
# Extracting each individual URLs for txt files containing data. 
def extractData(htmlOutput):
	table = htmlOutput.find('table')
	rows = []
	for row in table.findAll('a'):
		rows.append(str(row))
	urls = []
	for url in rows:
		url = homepage + url[9:81]
	 	data = getHTML(url)
	 	dataWriter(data,"raw_data_1990_1999.txt")

def dataWriter(data,filename):
	txt_file = open(filename, "a")
	txt_file.write(str(data))
	txt_file.close()
	print "Data written to file %s successfully" % filename 

# Parsing the webpage with Intercensal data 1990-1999	
output = getHTML("http://www.census.gov/popest/data/intercensal/st-co/characteristics.html")
template = fileTemplate(output)
data = extractData(output)










