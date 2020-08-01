import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://www.actu-comores.com/')
soup = BeautifulSoup(res.text,'html.parser')
section = soup.find_all('section',{'class':'site-content-wrap'})
url_list=[]
for sec in section:
    atag = (sec.find_all('a'))
    for href in atag:
        if href is not None:
            if href.get('href') not in url_list:
                if 'page' not in href.get('href'):
                    if '#respond' not in href.get('href'):
                        if '#comments' not in href.get('href'):
                            url_list.append(href.get('href'))

print(url_list)
print(len(url_list))

for url in url_list:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        dict1['content'] = []
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('h1',{'class':'entry-title'})
        for x in title:
            dict1['title'] = (x.text)
        for_img = soup.find_all('img')
        for img in for_img:
            if img.get('src').startswith('https://www.actu-comores.com/wp-content/uploads'):
                dict1['image'] = img.get('src')
                break
        for_content = soup.find_all('p')
        content_list=[]
        for content in for_content[2:]:
            content_list.append(content.text)
            if content.text =='Partager':
                break
        dict1['content'] = content_list
        dict1['url'] = url
        dict1['country'] = 'Comores'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass