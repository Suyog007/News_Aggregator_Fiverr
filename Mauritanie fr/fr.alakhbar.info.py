import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('http://www.fr.alakhbar.info/')
soup = BeautifulSoup(res.text,'html.parser')


news_list=[]
links = soup.find_all('div',{'class':'home_newstext'})
for link in links:
   
    save = link.find('a').get('href') 
    if "http" in save:
        continue
    news_list.append(save)
# links = soup.find_all('h3',{'class':'titre'})
# for link in links:
#     save = link.find('a').get('href') 
#     if "http" in save:
#         continue
#     news_list.append(save)
# links = soup.find_all('div',{'class':'texte'})
# for link in links:
#     save = link.find('a').get('href') 
#     if "http" in save:
#         continue
#     news_list.append(save)

print((news_list))


# for x in news_list:
#     dict1={}
#     res = requests.get('http://www.fr.alakhbar.info/' + x)
#     soup = BeautifulSoup(res.text,'html.parser')
#     title = soup.find('div',{'id':'content'})
#     dict1['title'] = title.find('h1').text
    
#     images = title.find_all('span')

#     for image in images:
#         img = image.find('img')
#         if img is not None:
#             dict1["image"] = 'http://www.fr.alakhbar.info/' + img.get('src')
       
#     images = soup.find_all('div',{'class':'tinymcewysiwyg'})
#     print(images)
#     content=[]
#     for image in images:
#         pp = image.find_all('p')
#         for p in pp:
#             if p.text is not None:
#                 content.append(p.text)
#     dict1['content'] = content
#     dict1['county'] = 'Mauritanie'
#     dict1['language'] ='fr'
#     dict1['URL'] = 'http://www.fr.alakhbar.info/' + x
    
    
 
#     x = mycol.insert_one(dict1)
#     print(dict1)
    