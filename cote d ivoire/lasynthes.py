import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://www.lasynthese.net/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('div',{'class':'vc_row wpb_row vc_row-fluid'})
link =[]
for x in soup:
    href = x.find_all('a')
    for hr in href:
        if hr.get('href') not in link:
            if 'category' not in hr.get('href'):
                link.append(hr.get('href'))

for url in link:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        url = url
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find('h2',{'class':'entry-title'})
        dict1['title'] = title.text
        img = soup.find('div',{'class':'entry-thumbnail'})
        img = (img.find('img').get('src'))
        dict1['image'] = img
        dict1['url'] = url
        dict1['country'] = 'cote d iviore'
        dict1['language'] = 'fr'
        print(dict1)
        # x = mycol.insert_one(dict1)
    except :
        pass
