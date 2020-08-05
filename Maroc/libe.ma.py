import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('https://www.libe.ma/')
soup = BeautifulSoup(res.text,'html.parser')


news_list=[]
links = soup.find_all('div',{'class':'titre'})
for link in links:
   
    save = link.find('a').get('href') 
    if "http" in save:
        continue
    news_list.append(save)
links = soup.find_all('h3',{'class':'titre'})
for link in links:
    save = link.find('a').get('href') 
    if "http" in save:
        continue
    news_list.append(save)
links = soup.find_all('div',{'class':'texte'})
for link in links:
    save = link.find('a').get('href') 
    if "http" in save:
        continue
    news_list.append(save)

# print((news_list))


for x in news_list:
    dict1={}
    res = requests.get('https://www.libe.ma/' + x)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.find('h1',{'class':'access'})
    if title is None:
        continue
    dict1['title'] = title.text
    
    
    image = soup.find('div',{'class':'photo shadow left'})
    
    
    if image is not None:
        imag= image.find('img')
        image_final = (imag.get('src'))
        dict1['image'] = image_final
       

    contents = soup.find('div',{'class':'access firstletter'})
    dict1['content'] = [contents.text]
    dict1['county'] = 'Maroc'
    dict1['language'] ='fr'
    dict1['URL'] = 'https://www.libe.ma/' + x
 
    x = mycol.insert_one(dict1)
    