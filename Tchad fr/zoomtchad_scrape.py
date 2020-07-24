# import requests
# from bs4 import BeautifulSoup
# url_list=[]
# header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# res = requests.get('http://zoomtchad.com/',headers= header)
# soup = BeautifulSoup(res.text,'html.parser')
# soup = soup.find_all('div',{'class':'content-wrapper'})
# for sin in soup:
#     atag = sin.find_all('a')
#     for tag in atag:
#         if tag.get('href') not in url_list:
#             if tag.get('href').startswith('http://zoomtchad.com/'):
#                 url_list.append(tag.get('href'))
#
# print(url_list)
# print(len(url_list))
# for url in url_list:
#     res = requests.get(url,headers=header)
#     soup= BeautifulSoup(res.text,'html.parser')
#     print(soup)
#     header1 = soup.find('h1',{'class':'post-title entry-title'})
#     print(header1)
#     if header1 is not None:
#         print(header1)
#     break