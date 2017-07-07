import requests
from bs4 import BeautifulSoup

def my_spider():
    url = "https://www.raspberrypi.org/"
    source_code = requests.get(url)
    sc = source_code.text
    soup = BeautifulSoup(sc,"html")
    for link in soup.findAll('a'):
    	href = link.get('href')
    	#title = link.string
    	#print (title)
    	print (href,"\n")
    	if not href=='#':
    		spymore(href)


def spymore(url):
	source_code = requests.get(url)
	sc = source_code.text
	soup = BeautifulSoup(sc,"html")
	for link in soup.findAll('a'):
		href = link.get('href')
		print(href,"/n")
my_spider()
