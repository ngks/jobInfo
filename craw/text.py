# coding:UTF-8

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url = target)
    req.encoding = req.apparent_encoding
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_ = 'listmain') 
    print(texts[0])