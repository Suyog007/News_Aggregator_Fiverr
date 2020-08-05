import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
header ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
link_list = []

for i in range(1,5):
    res = requests.get('https://www.burundi-forum.org/page/'+str(i))
    soup = BeautifulSoup(res.text,'html.parser')
    container = soup.find_all('div',{'class':'archive-grid-wrap clearfix'})
    for con in container:
        href = con.find_all('a')
        for h in href:
            tag = (h.get('href'))
            if tag not in link_list:
                if 'category' not in tag:
                    if tag.startswith('https://www.burundi-forum.org/'):
                        link_list.append(tag)
print(link_list)
print(len(link_list))
for one in link_list:
    try:
        dict1={}
        content_list=[]
        res = requests.get(one)
        soup = BeautifulSoup(res.text,'html.parser')
        head =soup.find_all('header',{'class':'page-header'})
        for he in head:
            hea = (he.text)
            hea = hea.replace('\n','')
            dict1['title'] = hea
        for_img = soup.find_all('figure',{'class':'nosidebar-image'})
        for img in for_img:
            dict1['image']= (img.find('img').get('src'))
        div = soup.find_all('div', {'class': 'home-main-content content-area'})
        for d in div:
            ptag = d.find_all('p')
            for p in ptag:
                ptag = p.text
                ptag = ptag.replace('\n', '')
                content_list.append(ptag)
        dict1['content'] = content_list
        dict1['url'] = one
        dict1['country'] = 'Burundi'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass
