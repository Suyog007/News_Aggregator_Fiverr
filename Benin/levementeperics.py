import requests
from bs4 import BeautifulSoup
import pymongo
header ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://levenementprecis.com/',headers=header)
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
link =[]
for x in soup:
    href = x.get('href')
    if href not in link:
        if href is not None:
            # if href.endswith('.html'):
                if 'category' not in href:
                        link.append(href)
for url in link:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        print(url)
        if not url.startswith('http://levenementprecis.com/'):
            url = 'http://levenementprecis.com/'+url
        res = requests.get(url,headers=header)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('h2',{'class':'entry-title post-title'})
        for x in title:
            if x is not None:
                dict1['title'] = x.text
        img = soup.find_all('figure',{'class':'alignright is-resized'})
        for x in img:
            if x is not None:
                img1 = x.find('img')
                if img1 is not None:
                    dict1['image'] = img1.get('src')
        if dict1['image'] =='':
            img = soup.find_all('figure', {'class': 'wp-block-image'})
            for x in img:
                if x is not None:
                    img1 = x.find('img')
                    if img1 is not None:
                        dict1['image'] = img1.get('src')
        dict1['url'] = url
        dict1['country'] = 'Benin'
        dict1['language'] = 'fr'
        if dict1['title'] == '':
            raise e
        print(dict1)
        x = mycol.insert_one(dict1)
    except Exception as e:
        print(e)
        pass
