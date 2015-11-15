import urllib2
from bs4 import BeautifulSoup
import codecs

count=0

for i in range (1947,2015):
    file = codecs.open("year"+unicode(i)+".txt", "w", encoding='utf8')
    

    soup=BeautifulSoup(urllib2.urlopen('http://www.bobborst.com/popculture/top-100-songs-of-the-year/?year='+ str(i), "lxml").read())
    #file.write("Year:" +unicode(i)+ "\n")
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        file.write(unicode(tds[1].text)+" - "+unicode(tds[2].text)+"\n")

    

