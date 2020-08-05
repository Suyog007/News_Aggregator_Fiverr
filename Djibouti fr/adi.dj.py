import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('http://www.adi.dj/')
soup = BeautifulSoup(res.text,'html.parser')
body = soup.find_all('div',{'class':'row'})
news_list=[]
for x in body:
    link = x.find_all('div',{'class':'col-lg-12 col-md-6 col-sm-12'})
    for anc in link:
        news_list.append(anc.find('a').get('href'))

for x in news_list:
    try:
        dict1={}
        res = requests.get(x)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find('div',{'class':'news-details-layout1'})
        title_final = (title.find('h1').text)
        dict1['title'] = title_final
        image_link = soup.find_all('ul',{'class':'post-info-dark mb-30'})
        for image in image_link:
            image_link = image.find('img')
            if image_link is not None:
                image_final = (image_link.get('src'))
                dict1['image'] = image_final
        content = soup.find_all('p')
        content_list=[]
        for con in content[:-2]:
            content_final = (con.text)
            content_list.append(content_final)
        dict1['content'] = content_list
        dict1['url'] = x
        dict1['county'] = 'Djibouti'
        dict1['language'] ='fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass
