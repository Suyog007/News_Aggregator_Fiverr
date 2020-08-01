import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://www.zinfos974.com/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
url_list=[]
for x in soup:
    if x.get('href').endswith('.html'):
        if x.get('href') not in url_list:
            if x.get('href').startswith('/'):
                url_list.append(x.get('href'))

print(url_list[16:])
print(len(url_list))
for url in url_list[17:]:
    dict1 = {}
    dict1['title'] = ''
    dict1['image'] = ''
    dict1['content'] = []
    url = 'https://www.zinfos974.com' + url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find('h1',{'class':'access'})
    print(title.text)
    for_image = soup.find_all('div', {'class': 'photo shadow top'})
    for img in for_image:
        dict1['image'] = (img.find('img').get('src'))
        break
    print(dict1['image'])
    break