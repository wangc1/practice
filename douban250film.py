#_*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests

j=1

print("-------------start getting the douban data--------------")
for i in range(0,10):
    print("------------the  "+str(i+1)+"  page--------------")
    respons=requests.get("https://movie.douban.com/top250"+"?start="+str(i*25))
    bs= BeautifulSoup(respons.text,"html.parser")
    movie=bs.find_all("img")
    href=bs.select("div > a[href]")
    for a in href[8:-12]:
        res=requests.get(a.get("href"))
        bbs=BeautifulSoup(respons.text,"html.parser")

    rating_num=bs.select('span[class*=rating_num]')
    for i in zip(movie,rating_num):
        print(str(j)+i[0].get('alt')+i[1].text)
        j=j+1
print("-----------finished--------------")
