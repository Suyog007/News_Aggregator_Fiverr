import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://zenga-mambu.com/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
url_list=[]
for x in soup:
    if x is not None:
        if x.get('href') is not None:
            if (x.get('href')).startswith('http://zenga-mambu.com/20'):
                if x.get('href') not in url_list:
                    url_list.append(x.get('href'))
print(url_list)
for url in url_list:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        dict1['content'] = []
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('h1',{'class':'entry-title'})
        for h1 in title:
            dict1['title'] = (h1.text)
        for_image = soup.find_all('div',{'class':'post-thumbnail full-width-image'})
        for x in for_image:
            if x is not None:
                dict1['image'] = (x.find('img').get('src'))
        for_content = soup.find_all('p')
        content_list = []
        for x in for_content[1:-2]:
            if '\n' not in x.text:
                content_list.append(x.text)
        dict1['content'] = content_list[:-1]
        if dict1['content'] !=[]:
            dict1['url'] = url
            dict1['country'] = 'Congo brazzavile'
            dict1['language'] = 'fr'
            print(dict1)
            x = mycol.insert_one(dict1)
    except:
        pass