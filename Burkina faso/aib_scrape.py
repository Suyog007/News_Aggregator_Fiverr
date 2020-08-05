import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']
header ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
res = requests.get('https://www.aib.media/',headers = header)
soup = BeautifulSoup(res.text,'html.parser')
container = soup.find_all('div',{'class':'td_block_inner td-column-2'})
link_list=[]
for con in container:
    href = con.find_all('a')
    for hr in href:
        atag=hr.get('href')
        if atag not in link_list:
            if 'category' not in atag:
                link_list.append(atag)

for one in link_list:
    try:
        dict1={}
        content_list=[]
        res = requests.get(one,headers=header)
        soup = BeautifulSoup(res.text,'html.parser')
        head = soup.find_all('h1',{'class':'entry-title'})
        for h1 in head:
            hea = (h1.text)
            hea = hea.replace('\n','')
            dict1['title'] = hea
        for_image = soup.find_all('div',{'class':'td-post-featured-image'})
        for img in for_image:
            dict1['image'] = (img.find('img').get('src'))
        for_content = soup.find_all('div',{'class':'td-post-content tagdiv-type'})
        for con in for_content:
            ptag = con.find_all('p')
            for tag in ptag:
                ta = (tag.text)
                ta = ta.replace('\n','')
                ta = ta.replace('\xa0','')
                content_list.append(ta)
        dict1['content'] = content_list
        dict1['url'] = one
        dict1['country'] = 'Burkina Faso'
        dict1['language'] = 'fr'
        print(dict1)
        x = mycol.insert_one(dict1)
    except:
        pass