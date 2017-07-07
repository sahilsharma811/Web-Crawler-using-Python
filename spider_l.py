import requests
from lxml import html
import csv

def my_spider():
    url = "https://www.raspberrypi.org/"

    source_code = requests.get(url)
    tree = html.fromstring(source_code.content)
    
    linkss = tree.xpath('//a/@href')

    #print (linkss,"\n")

    l= len(linkss)	
    with open("my_links.csv","w") as ob:
    	i=0
    	while i<l:
    		ob.write(linkss[i]+"\n")
    		i+=1
    ob.close()
my_spider()
