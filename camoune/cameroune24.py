import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://cameroun24.net/')
soup = BeautifulSoup(res.text,'html.parser')
content = soup.find_all('div',{'class':'content_top'})
url_list=[]
for ab in content:
    href =ab.find_all('a')
    for tag in href:
        if tag is not None:
            if tag.get('href') not in url_list:
                url_list.append(tag.get('href'))

bottom_content = soup.find_all('div',{'class':'content_bottom'})
for ab in content:
    href =ab.find_all('a')
    for tag in href:
        if tag is not None:
            if tag.get('href') not in url_list:
                if tag.get('href').endswith('.html'):
                    url_list.append(tag.get('href'))
print(len(url_list))
for url in url_list:
    try:
        dict1={}
        res = requests.get('http://cameroun24.net/'+url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('div',{'class':'single_page_area'})
        for t in title:
            dict1['title'] = (t.find('h2').text)
        for t in title:
            for_img = t.find_all('div',{'class':'single_page_content'})
            for img in for_img:
                image = (img.find('img').get('src'))
                image = 'http://cameroun24.net/'+image
                dict1['image'] = image
        content_list=[]
        for t in title:
            ptag = t.find_all('p')
            for tag in ptag[1:-1]:
                content_list.append(tag.text)
        dict1['content'] = content_list
        dict1['url'] = 'http://cameroun24.net/'+url
        dict1['country'] = 'Cameroune'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass