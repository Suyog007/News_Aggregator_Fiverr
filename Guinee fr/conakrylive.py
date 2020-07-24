import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://conakryinfos.com/')
soup = BeautifulSoup(res.text,'html.parser')
url_list=[]
soup = soup.find_all('div',{'class':'bs-listing bs-listing-listing-blog-1 bs-listing-single-tab'})
for link in soup:
    href = link.find_all('a')
    for x in href:
        if not x.get('href').startswith('https://conakryinfos.com/category/'):
            if x.get('href') not in url_list:
                url_list.append(x.get('href'))

for urls in url_list:
    try:
        dict1={}
        res = requests.get(urls)
        soup = BeautifulSoup(res.text,'html.parser')
        for_header = soup.find_all('div',{'class':'post-header post-tp-1-header'})
        for head in for_header:
            header = (head.text)
            header = header.replace('\n','')
            header = header.replace('?','')
            dict1['title'] = header
        for_image = soup.find_all('div',{'class':'single-featured'})
        for img in for_image:
            dict1['image'] = (img.find('img').get('src'))
        for_content = soup.find_all('div',{'class':'pf-content'})
        p_list =[]
        for con in for_content:
            ptag = con.find_all('p')
            for x in ptag:
                p_list.append(x.text)
        dict1['content'] = p_list
        dict1['url'] = urls
        dict1['county'] = 'Guinee'
        dict1['language'] = 'fr'
        x = mycol.insert_one(dict1)
        print(dict1)
    except:
        pass