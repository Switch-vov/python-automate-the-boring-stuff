import requests
import bs4

exampleFile = open('example.html')
soup = bs4.BeautifulSoup(exampleFile.read(), "lxml")
elems = soup.select('#author')
ele = elems[0]
print(type(elems))
print(len(elems))
print(type(ele))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
print(elems[0].get('id'))
