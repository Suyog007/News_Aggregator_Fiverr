import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://lesechos-congobrazza.com/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
link =[]
for x in soup:
    href = x.get('href')
    if href not in link:
        if href is not None:
                if 'category' not in href:
                    link.append(href)


for url in link:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        if not url.startswith('https://lesechos-congobrazza.com'):
            url = 'https://lesechos-congobrazza.com/'+url
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('h1',{'class':'article-title'})
        for x in title:
            if x is not None:
                dict1['title'] = x.text
        img = soup.find_all('div',{'class':'pull-none item-image article-image article-image-full'})
        for x in img:
            if x is not None:
                image = (x.find('img'))
                if image is not None:
                    dict1['image'] = 'https://lesechos-congobrazza.com'+image.get('src')
        dict1['url'] = url
        dict1['country'] = 'Congo brazzavile'
        dict1['language'] = 'fr'
        if dict1['title'] == '':
            raise e
        print(dict1)
        x = mycol.insert_one(dict1)
    except Exception as e:
        print(e)
        pass
