import requests
from bs4 import BeautifulSoup
import pymongo
header ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://lesaffairesbf.com/',headers=header)
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
        res = requests.get(url,headers=header)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('h1')
        for x in title:
            if x is not None:
                dict1['title'] = x.text
        img = soup.find_all('div',{'id':'media-wrapper'})
        for x in img:
            if x is not None:
                image = (x.find('img'))
                if image is not None:
                    dict1['image'] = image.get('src')
        dict1['url'] = url
        dict1['country'] = 'Burkina Faso'
        dict1['language'] = 'fr'
        if dict1['title'] == '':
            raise e
        print(dict1)
        x = mycol.insert_one(dict1)
    except Exception as e:
        print(e)
        pass
