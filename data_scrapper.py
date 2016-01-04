# Web Scrapper 
# Import Libraries to access and retrieve data from HTML and XML files

import requests 
from BeautifulSoup import BeautifulSoup
import csv

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
	#print data
	header = [['Year','FIPS_state_code','FIPS_county_code','Age_group','Race-Sex','Ethnic_origin','population']]
	csvWriter('data_1990_1999.csv', 'w', header)
	print "Template creation successful"

def csvWriter(fileName, mode, data):
	open_csv = open(fileName, mode, newline='')
	a = csv.writer(open_csv)
	a.writerows(data)
	open_csv.close()

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
	 	csvWriter('data_1990_1999.csv', 'a', data)
	 	print "data write successful"

def getContent(url):
	response = requests.get(url)
	data = BeautifulSoup(response.content)

# Parsing the webpage with Intercensal data 1990-1999	
output = getHTML("http://www.census.gov/popest/data/intercensal/st-co/characteristics.html")
template = fileTemplate(output)
data = extractData(output)








