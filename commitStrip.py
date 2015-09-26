from bs4 import BeautifulSoup
import urllib2
import urllib
import sys
import os


baseURL = 'http://commitstrip.com/en/'
path = raw_input('Enter the path you want to download')


reload(sys)
sys.setdefaultencoding('utf8')




response = urllib2.urlopen(baseURL)
mainPage = BeautifulSoup(response.read(),'html.parser')
print(len(mainPage.find('li',class_="collapsing archives expand")))
for yearPage in mainPage.find_all("li",class_="collapsing archives expand"):
	year = yearPage.find("a").contents[0]
	yearPath = path + year + "/"

	print('Yo')
	if year != '2015':
		print('Hello')

		if not os.path.exists(yearPath):
			os.makedirs(yearPath)
			
		for monthItem in yearPage.find_all("li",class_="collapsing archives "):
			monthAnchor = monthItem.find("a")
			month = monthAnchor.contents[0]
			monthPath = yearPath + month + '/'
			if not os.path.exists(monthPath):
				os.makedirs(monthPath)
			monthlyPage = BeautifulSoup(urllib2.urlopen(monthAnchor['href']))
			for element in monthlyPage.find_all("div",class_="excerpt"):
				anchor = element.find("a")
				response2 = urllib2.urlopen(anchor['href'])
				singleStrip = BeautifulSoup(response2.read(),'html.parser')
				for strip in singleStrip.find_all("div",class_="entry-content"):
					comicName = anchor.contents[3].contents[3].contents[0] + '.jpg'
					#print((strip.contents[1].contents[0])['src'])
					strip = strip.find("img")
					try:
						urllib.urlretrieve(strip['src'].encode('utf-8'),monthPath+comicName)
					except Exception, e:
						print(strip)
						pass
					
					print(comicName+' done')
		

