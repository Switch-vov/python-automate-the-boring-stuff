import requests
import os
import bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,"lxml")
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
        continue
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s...' % comicUrl)

        imagePath = os.path.join('xkcd', os.path.basename(comicUrl))
        if not os.path.exists(imagePath):
            res = requests.get(comicUrl)
            res.raise_for_status()
            imageFile = open(imagePath, 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    prevLink = soup.select('a[rel=prev]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
