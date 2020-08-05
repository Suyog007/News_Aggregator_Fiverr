import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
link_list = []
for i in range(1,5):
    res= requests.get('https://lanouvelletribune.info/tag/benin/page/'+str(i))
    soup = BeautifulSoup(res.text,'html.parser')
    container = soup.find_all('div',{'class':'jeg_block_container'})
    for con in container[:-1]:
        href = con.find_all('a')
        for x in href:
            get = (x.get('href'))
            if 'author' not in get:
                if '#comments' not in get:
                    if get not in link_list:
                        link_list.append(get)
print(len(link_list))

for one in link_list:
    try:
        dict1={}
        content_list=[]
        res = requests.get(one)
        soup = BeautifulSoup(res.text,'html.parser')
        head = soup.find('div',{'class':'entry-header'})
        head = (head.text)
        head = head.replace('\n','')
        dict1['head'] = head
        content = soup.find_all('div',{'class':'entry-content no-share'})
        for con in content:
            co = (con.text)
            co = co.replace('\n','')
            content_list.append(co)
        for_image = soup.find_all('div',{'class':'thumbnail-container'})
        for img in for_image:
            dict1['image'] = (img.find('img').get('src'))
        dict1['content'] = content_list
        dict1['url'] = one
        dict1['country'] = 'Benin'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass
