# coding:UTF-8

import requests
from bs4 import BeautifulSoup
import sys

class my_craw(object):
    def __init__(self, server, target):
        self.server = server
        self.target = target
        self.names = []
        self.urls = []
        self.nums = 0

    def get_urls(self):
        # req = requests.get(url = self.target)
        # req.encoding = req.apparent_encoding
        # html = req.text
        # fo = open('new.txt', 'w+')
        # fo.write(html)
        # fo.close()
        fo = open('new.txt')
        html = fo.read()
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
        

if __name__ == '__main__':
    craw = my_craw('http://www.biqukan.com/', 'http://www.biqukan.com/1_1094/')
    craw.get_urls()

    # req = requests.get(url = target)
    # req.encoding = req.apparent_encoding
    # html = req.text
    # bf = BeautifulSoup(html)
    # texts = bf.find_all('div', class_ = 'listmain') 
    # print(texts[0])