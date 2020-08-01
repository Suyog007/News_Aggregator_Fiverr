import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('http://www.gabonews.com/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
url_list=[]
for x in soup:
    if '/article/' in x.get('href'):
        if x.get('href').startswith('fr'):
            if x.get('href') not in url_list:
                url_list.append(x.get('href'))
print(url_list)
print(len(url_list))

for url in url_list:
    try:
        dict1 = {}
        dict1['title'] = ''
        dict1['image'] = ''
        dict1['content'] = []
        url = 'http://www.gabonews.com/' + url
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find('h2')
        dict1['title'] = (title.text)
        for_image = soup.find('span',{'class':'bloc-img-post'})
        image = 'http://www.gabonews.com/'+(for_image.find('img').get('src'))
        dict1['image'] = image
        for_content = soup.find_all('p')
        content_list=[]
        for con in for_content[:-8]:
            content_list.append(con.text)
        dict1['content'] = content_list
        dict1['url'] = url
        dict1['country'] = 'cote d iviore'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass