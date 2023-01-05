

import requests
from bs4 import BeautifulSoup
import db
from datetime import datetime as dt #抓日期函示庫

today=dt.today() #抓今日的日期格式
todays=today.strftime('%Y-%m-%d') #將設定好的日期格式轉換為字串使用

url="https://tw.buy.yahoo.com/search/product"

payload={'p':'女鞋'}

data=requests.get(url,params=payload).text

soup=BeautifulSoup(data,'html.parser')

goods=soup.find_all('ul',class_='gridList')[-1]

allgoods=goods.find_all('a','sc-jHNicF bMmwdY')
# print(allgoods)
cursor=db.conn.cursor()

for row in allgoods:

    link=row.get('href')
    photo=row.find('img').get('srcset')
    title=row.find('span',class_='sc-Arkif sc-khIgEk sc-eKYRIR gPtwee hvLVyh tOwMo').text
    price=row.find('span',class_='sc-Arkif fYIZbn').text
    price=price.replace('$','').replace(',','')

    photos=photo.split()[0]

    print(link)
    print(photos)
    print(title)
    print(price)
    print()


    sql = "select * from goods where name='{}' ".format(title)
    
    cursor.execute(sql)
    
    db.conn.commit()
    
    if cursor.rowcount==0: #表示沒有該產品
        sql="insert into goods(name,price,goods_url,photo_url,create_date,discount) values('{}','{}','{}','{}','{}','0')".format(title,price,link,photos,todays)
    
        cursor.execute(sql)
        db.conn.commit()
    
    
db.conn.close()   
    
    
    

