import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
res = requests.get('https://www.laotravoz.info/')
soup = BeautifulSoup(res.text,'html.parser')
soup = soup.find_all('a')
url_list=[]
for x in soup:
    if x.get('href').endswith('.html'):
        if x.get('href') not in url_list:
            if x.get('href').startswith('/'):
                url_list.append(x.get('href'))

print(url_list)
print(len(url_list))

for url in url_list:
    dict1 = {}
    dict1['title'] = ''
    dict1['image'] = ''
    dict1['content'] = []
    url = 'https://www.laotravoz.info' + url
    url = 'https://www.laotravoz.info/Le-Senegal-et-la-Guinee-equatoriale-discuteront-des-investissements-post-Covid-en-Afrique-avec-le-secteur-prive-allemand_a3634.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find('h1',{'class':'access'})
    dict1['title'] = (title.text)
    for_image = soup.find_all('div',{'class':'photo shadow top'})
    for img in for_image:
        dict1['image'] = (img.find('img').get('src'))
        break
    for_content= soup.find('div',{'class':'texte'})
    print(for_content.text)
    content_list=[]
    # for con in for_content:
    #     ptag = con.text
    #     content_list.append(ptag)

    print(dict1)
    break