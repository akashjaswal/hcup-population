# Web Scrapper 
# Import Libraries to access and retrieve data from HTML and XML files

import requests 
from BeautifulSoup import BeautifulSoup

# Parsing the webpage with Intercensal data 1990-1999
url = "http://www.census.gov/popest/data/intercensal/st-co/characteristics.html"
response = requests.get(url)
htmlOutput = response.content

soup = BeautifulSoup(htmlOutput)
table = soup.find('table')

rows = []
for row in table.findAll('a'):
	rows.append(str(row))

# Extracting each individual URLs for txt files containing data. 
urls = []
homepage = "http://www.census.gov"
for url in rows:
	url = homepage + url[9:81]
	urls.append(url)
print urls



