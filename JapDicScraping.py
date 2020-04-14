from typing import Dict
import requests
from bs4 import BeautifulSoup
import re

insert = input('Введите слово: ')
payload = {'q':insert,'pg':'0','dic_jardic':'1','sw':'1920'}
site = 'http://www.jardic.ru/search/search_r.php'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(site, params=payload, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

result_word = soup.findAll("span",{"style":"color: #7F0000;"})
result_kanji = soup.findAll("span",{"style":"color: #00007F;"})
result_trans = soup.findAll("span",{"style":"color: #000000;"})

try:
    for i in range(10):
        print(result_word[i].text + ' (' + result_kanji[i].text + ')' + ' - ' + re.sub(r'•','\n', result_trans[i].text))
        i+=1
except IndexError:
    print('\n'+"*больше ничего нет*")
