import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://www.lebanco.net/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
url_list=[]
for x in soup:
    if x.get('href').startswith('news/'):
        if x.get('href') not in url_list:
            url_list.append(x.get('href'))

print(len(url_list))
print(url_list)

for url in url_list:
    try:
        dict1={}
        dict1['title'] = ''
        dict1['image'] = ''
        dict1['content'] = []
        url = 'https://www.lebanco.net/'+url
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        title = soup.find('h1',{'class':'mvp-post-title left entry-title'})
        dict1['title'] = (title.text)
        for_image = soup.find('div',{'id':'mvp-post-feat-img'})
        dict1['image'] = (for_image.find('img').get('src'))
        for_content = soup.find_all('div',{'id':'mvp-content-main'})
        content_list=[]
        for con in for_content:
            ptag = (con.find_all('p'))
            for x in ptag:
                content_list.append(x.text)
        dict1['content'] = content_list
        dict1['url'] = url
        dict1['country'] = 'cote d iviore'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass