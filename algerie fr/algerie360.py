import requests
from bs4 import BeautifulSoup
import pymongo
header ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://www.algerie360.com/',headers=header)
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
        if not url.startswith('https://www.algerie360.com/'):
            url = 'https://www.algerie360.com/'+url
        res = requests.get(url,headers=header)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find_all('span',{'class':'breadcrumb_last'})
        for x in title:
            if x is not None:
                dict1['title'] = x.text
        img = soup.find_all('div',{'class':'thumb thumb--size-6 mb-4'})
        for x in img:
            x = str(x)
            count =x.find('"url(')
            count2= x.find(".jpg')"'')
            dict1['image'] = (x[count+6:count2+4])

        dict1['url'] = url
        dict1['country'] = 'Algerie'
        dict1['language'] = 'fr'
        if dict1['title'] == '':
            raise e
        print(dict1)
        x = mycol.insert_one(dict1)
    except Exception as e:
        print(e)
        pass
