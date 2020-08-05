import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['freelance']
mycol = mydb['api']

res = requests.get('http://www.inovaovao.com/')
soup = BeautifulSoup(res.text,'html.parser')


news_list=[]
link = soup.find('div',{'class':'bloc_c'})

save = link.find('a').get('href') 
news_list.append(save)
links = soup.find_all('div',{'class':'bloc_c'})

for link in links:
    spans = link.find_all('span')

    for span in spans: 
        aa = span.find_all('a')
        for a in aa:
            news_list.append(a.get('href'))

    






    



for x in news_list:
    dict1={}
    res = requests.get('http://www.inovaovao.com/'+x)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.find('div',{'class':'txt_rub'})
    title_final = (title.find('h2').text)
    dict1['title'] = title_final
  
    imag= title.find('img')
    if imag is not None:
        image_final = (imag.get('src'))
        dict1['image'] = 'http://www.inovaovao.com/' +image_final

        

          

    content_list=[]
    content1 = title.find_all('p')
  
    
   
    for con in content1:
        content_final = (con.text)
        if "N.A" in content_final:
            break
        content_list.append(content_final)
    dict1['content'] = content_list
    dict1['county'] = 'Madagascar'
    dict1['language'] ='fr'
    dict1['URL'] = 'http://www.inovaovao.com/'+x
    x = mycol.insert_one(dict1)
