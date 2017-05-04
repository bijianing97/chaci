#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
import urllib.request
import urllib.parse 
import json 
import webbrowser
from bs4 import BeautifulSoup
import sys
import sqlite3


def translate(word):
  content = word
  url = 'http://fanyi.youdao.com/openapi.do'  
  key = '1829235709' 
  keyfrom = 'bjnfanyi' 
  allurl = url + '?keyfrom=' + keyfrom + '&key='+  key + '&type=data&doctype=json&version=1.1&q=' + content
  response = urllib.request.urlopen(allurl)
  html = response.read().decode('utf-8')
  result = json.loads(html)
  newresult = result.get('basic').get('explains')
  for x in newresult:
      print(x)
  save_word(word)


   
def save_word(word):
  content = word
  url = "http://127.0.0.1:8000/jilu/add?word="
  response = urllib.request.urlopen(url + content)


def show_word():
  sys.path.append("libs")
  url = "http://127.0.0.1:8000/jilu/"
  webbrowser.open(url)
  print('查询历史已显示在浏览器中。')

def daochu():
  url = "http://127.0.0.1:8000/jilu/"
  response = urllib.request.urlopen(url)
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  result = []
  for x in soup.findAll('td'):
      result.append(x.string.split(' ')[0])
  f = open('.//word_list.txt', 'w')
  for word in result:
        f.write('%s\n' % word)
  f.close()
  print('单词查询记录已导出到\\word_list.txt文件。')
  
    
def minglingtishi():    
    print('               命令说明         \n')
    print('输入    danci 单词      进行单词查询\n')
    print('输入    chakan          用浏览器查看单词查询记录\n ')
    print('输入    daochu          导出单词查询记录到./word_list.txt文件\n')
    print('输入    quit            退出本程序\n')
    print('\n\n\n') 
   

minglingtishi()
while True: 
     msg = input ('输入你的命令(quit结束):\n') 
     if msg == 'quit':
        break
     elif msg =='chakan':
        show_word()
     elif msg =='daochu':
        daochu()
     else:
        [order, word] = msg.split(' ')
        if order == 'danci':
            translate(word)

      
