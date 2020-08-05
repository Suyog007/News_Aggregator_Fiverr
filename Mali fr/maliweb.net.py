import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('https://www.maliweb.net/')
soup = BeautifulSoup(res.text,'html.parser')


news_list=[]
links = soup.find_all('h3',{'class':'entry-title td-module-title'})
for link in links:
    save = link.find('a').get('href') 
    news_list.append(save)

for x in news_list:
    dict1={}
    res = requests.get(x)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.find('h1',{'class':'entry-title'})
    dict1['title'] = title.text
    
    
    image = soup.find('div',{'class':'td-post-featured-image'})
    
    
    if image is not None:
        imag= image.find('a')
        image_final = (imag.get('href'))
        dict1['image'] = image_final
       

    contents = soup.find('div',{'class':'td-post-content tagdiv-type'})
    pp = contents.find_all('p')
          

    content_list=[]
   
  
    
   
    for p in pp:
        content_final = (p.text)
        content_list.append(content_final)
    dict1['content'] = content_list
    dict1['county'] = 'Mali'
    dict1['language'] ='fr'
    dict1['URL'] = x
    x = mycol.insert_one(dict1)
