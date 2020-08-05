import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('https://fr.igihe.com/')
soup = BeautifulSoup(res.text,'html.parser')
body = soup.find_all('div',{'class':'article-wrap'})


news_list=[]
for x in body:
    link = x.find_all('span',{'class':'homenews-title'})
    for anc in link:
        news_list.append(anc.find('a').get('href'))
for x in body:
    link = x.find_all('span',{'class':'time text-center'})
    for anc in link:
        news_list.append(anc.find('a').get('href'))



for x in news_list:
    dict1={}
    res = requests.get('https://fr.igihe.com/'+x)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.find('div',{'class':'wrap-article'})
    title_final = (title.find('h3').text)
    dict1['title'] = title_final
    image_link = soup.find_all('div',{'class':'col col-lg-5'})
    for image in image_link:
        imag= image.find('img')
        # print(imag)
        if imag is not None:
            image_final = (imag.get('src'))
            dict1['image'] = 'https://fr.igihe.com/'+ image_final
          

    content_list=[]
    heading1 = soup.find('span',{'class':'surtitre'})
    content1 = heading1.find('p')
    content_list.append(content1.text)
    heading2 = soup.find('div',{'class':'fulltext margintop10'})
    content2 = soup.find_all('p')
   
    
   
    for con in content2[2:]:
        content_final = (con.text)
        content_list.append(content_final)
    dict1['content'] = content_list
    dict1['county'] = 'Rwanda'
    dict1['language'] ='fr'
    dict1['URL'] = 'https://fr.igihe.com/'+x
    # print(dict1)
    x = mycol.insert_one(dict1)
