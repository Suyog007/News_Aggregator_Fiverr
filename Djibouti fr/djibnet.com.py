# import requests
# from bs4 import BeautifulSoup
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient['freelance']
# mycol = mydb['api']
#
# res = requests.get('http://www.djibnet.com/news/','html.parser')
# soup = BeautifulSoup(res.text,'html.parser')
# soup = soup.find_all('div',{'class':'dj_section'})
# link_list =[]
# for link in soup:
#     dt = link.find_all('dt')
#     for x in dt:
#         atag = (x.find('a'))
#         if atag is not None:
#             atag = atag.get('href')
#             if atag.startswith('http')