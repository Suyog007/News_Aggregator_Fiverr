import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://news.abangui.com/')
soup = BeautifulSoup(res.text,'html.parser')
content = soup.find_all('div',{'id':'module'})
url_list=[]
for con in content:
    href = con.find_all('a')
    for tag in href:
        if tag is not None:
            if tag.get('href').startswith('http://news.aBangui'):
                if tag.get('href').endswith('.html'):
                    if tag.get('href') not in url_list:
                        url_list.append(tag.get('href'))

for url in url_list:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        head = soup.find_all('span',{'class':'FontArticleMainTitle'})
        for title in head:
            dict1['title'] = (title.text)
        if dict1['title'] == '':
            head = soup.find_all('h1',{'class':'FontArticleMainTitle'})
            for title in head:
                dict1['title'] = (title.text)
        for_img = soup.find_all('img',{'class':'imgArt'})
        for img in for_img:
            dict1['image'] = (img.get('src'))
        if dict1['image'] == '':
            for_img = soup.find_all('div',{'align':'center'})
            for x in for_img:
                y = (x.find('img'))
                if y is not None:
                    img = (y.get('src'))
                    if 'img_photos' in img:
                        dict1['image'] = img
        for_content = soup.find_all('span',{'class':'FullArticleTexte'})
        content_list=[]
        for text in for_content:
            content_list.append(text.text)
        dict1['content'] = content_list
        dict1['url'] = url
        dict1['country'] = 'Centre Afrique'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass
