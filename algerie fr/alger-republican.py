import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://www.alger-republicain.com/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a',{'class':'titre'})
link =[]
for sou in soup:
    link.append(sou.get('href'))
for xx in link:
    try:
        dict1={}
        site = 'http://www.alger-republicain.com/'+xx
        res = requests.get(site)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find('div',{'class':'titre'})
        title = title.text
        title = title.replace('\xa0','')
        title=title.replace('>>','')
        title =  title.replace('<<','')
        dict1['title'] = title
        description = soup.find('div',{'class':'description'})
        description = description.text
        description = description.replace('\n','')
        description = description.replace('\xa0','')
        dict1['content'] = description
        source = site
        dict1['url'] = source
        dict1['image'] = ''
        dict1['county'] = 'Algerie'
        dict1['language'] = 'fr'
        x = mycol.insert_one(dict1)
    except:
        pass