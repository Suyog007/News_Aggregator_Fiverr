import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://lanation.dj/')
soup =BeautifulSoup(res.text,'html.parser')
link_list=[]
soup = soup.find_all('div',{'class':'td-main-content-wrap td-main-page-wrap td-container-wrap'})
for x in soup:
    href = x.find_all('a')
    for h in href:
        if h.get('href') not in link_list:
            lin = h.get('href')
            if lin not in link_list:
                if lin[20:28] !='category':
                    if lin.startswith('http'):
                        if not lin.endswith('#respond'):
                            link_list.append(h.get('href'))

print(len(link_list))
for one in link_list[:-1]:
    try:
        print(one)
        dict1={}
        content_list=[]
        res = requests.get(one)
        soup = BeautifulSoup(res.text,'html.parser')
        header = soup.find_all('header',{'class':'td-post-title'})
        for head in header:
            head = (head.find('h1',{'class':'entry-title'}))
            dict1['title'] = (head.text)
        image = soup.find_all('div',{'class':'td-post-featured-image'})
        for img in image:
            img = img.find('img').get('src')
            dict1['image'] = img
        content = soup.find('div',{'class':'td-post-content'})
        con_list = (content.find_all('p'))
        for lis in con_list:
            content = lis.text
            content_list.append(content)
        dict1['content'] = content_list
        dict1['url'] = one
        dict1['county'] = 'Djibouti'
        dict1['language'] ='fr'
        x = mycol.insert_one(dict1)

    except:
        print('errir')
        print(one)
