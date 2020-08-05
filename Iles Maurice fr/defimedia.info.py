import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('https://defimedia.info/')
soup = BeautifulSoup(res.text,'html.parser')
body = soup.find_all('div',{'role':'main'})


news_list=[]
for x in body:
    link = x.find_all('div',{'class':'article-teleplus-inner'})
    news_list = []
    for a in link:
        save = a.find('a').get('href')
        if "http" not in save:
            news_list.append(save)
print(news_list[0])
 
  
    

    



for x in news_list:
    dict1={}
    res = requests.get('https://defimedia.info/'+x)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.find('div',{'class':'col-sm-12','role':'heading'})
    title_final = (title.find('h1').text)
    dict1['title'] = title_final
    print(title_final)
    image_link = soup.find_all('div',{'class':'content'})
    for image in image_link:
        imag= image.find('img')
        # print(imag)
        if imag is not None:
            image_final = (imag.get('src'))
            dict1['image'] = image_final
            break
        video = image.find('iframe')
        if video is not None:
            dict1['image'] = video.get('src')

          

    content_list=[]
    heading1 = soup.find('div',{'class':'content'})
    content1 = heading1.find_all('p')
  
    
   
    for con in content1:
        content_final = (con.text)
        content_list.append(content_final)
    dict1['content'] = content_list
    dict1['county'] = 'Illes Maurice'
    dict1['language'] ='fr'
    dict1['URL'] = 'https://defimedia.info'+x
    # print(dict1)
    x = mycol.insert_one(dict1)
