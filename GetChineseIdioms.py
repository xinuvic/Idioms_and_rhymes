# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:57:50 2019

@author: xin

steps：
1. find all 成语 from URL 'http://chengyu.t086.com/'
file_o record_only_cy.txt 只记录成语
file record.txt 记录成语及对应拼音
file_del record_del.txt 只记录成语及韵母（去除声母）
2. find 成语 with the same 韵母
record_colle.txt 记录同韵母的成语，从第一行起循环遍历，将相同韵母的成语记录在同一行，方便去除重复项
record_colle_del_copy.txt 遍历，去除字符串重复的行

This code is for step 1, get all chinese idioms from the website and their corresponding pinyin

"""

import requests
from bs4 import BeautifulSoup
import sqlite3
import uuid
import hanzi2pinyin


conn = sqlite3.connect("idiombase.db3")  #创建sqlite.db数据库
print ("open database success")
conn.execute("drop table IF EXISTS idiom")
query = """create table IF NOT EXISTS idiom(
    id VARCHAR(50),
    word VARCHAR(50)
);"""
conn.execute(query)
print ("Table created successfully")

all_url = 'http://chengyu.t086.com/'


#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://chengyu.t086.com/'
}

word=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
#word=['A']
file_o=open("record_only_cy.txt",'w',encoding='utf-8')
file = open("record.txt",'w',encoding='utf-8')
file_del = open("record_del.txt",'w',encoding='utf-8')

test = hanzi2pinyin.PinYin()
test.load_word('word.data')
shengmu =['zh','ch','sh','b','p','m','f','d','t','n','l','g','k','h','j','q','x','z','c','s','r','y','w']

for w in word:

    for n in range(1,100):

        url=all_url+'list/'+w+'_'+str(n)+'.html'
       
        start_html = requests.get(url,headers = Hostreferer)
        if(start_html.status_code==404):
            break
        start_html.encoding='gb2312'
        soup = BeautifulSoup(start_html.text,"html.parser")

        listw = soup.find('div',class_='listw')
        
        lista = listw.find_all('a')
        for p in lista:
            topinyin = test.hanzi2pinyin_split(string=p.text, split=" ", firstcode=False)
            topinyin_delete_sm=topinyin
            for i in shengmu:
                if ' '+i in topinyin:                
                    topinyin_delete_sm=topinyin_delete_sm.replace(' '+i,' ')
            file_o.write(p.text+"\n")
            file.write(p.text+' '+topinyin+"\n")
            file_del.write(p.text+' '+topinyin_delete_sm+"\n")
            ids=str(uuid.uuid1())
            query = "insert into idiom (id,word) values ('"+ids+"','"+p.text+"');"
            conn.execute(query)
            conn.commit()


file_o.close()            

file.close()

file_del.close()

