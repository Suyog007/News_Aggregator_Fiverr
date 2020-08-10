import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://lejournaldemayotte.yt/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
link =[]
for x in soup:
    href = x.get('href')
    if href not in link:
        if href is not None:
            if href.startswith('https://lejournaldemayotte.yt/'):
                if 'category' not in href:
                        link.append(href)

print(link)
for url in link:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        if not url.startswith('https://lejournaldemayotte.yt/'):
            url = 'https://lejournaldemayotte.yt/'+url
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('h1',{'class':'entry-title'})
        for x in title:
            if x is not None:
                dict1['title'] = x.text
        img = soup.find_all('figure')
        for x in img:
            if x is not None:
                image = (x.find('img'))
                if image is not None:
                    dict1['image'] = image.get('src')
        dict1['url'] = url
        dict1['country'] = 'Comores'
        dict1['language'] = 'fr'
        if dict1['title'] == '':
            raise e
        print(dict1)
        x = mycol.insert_one(dict1)
    except Exception as e:
        print(e)
        pass
