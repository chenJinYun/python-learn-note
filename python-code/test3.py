# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:33:12 2018

@author: CHENKI
"""


#request
#opener = urllib2.build_opener()

#opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'), ('Accept', 'application/json, text/javascript'), ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6')]
"""
url = 'https://www.baidu.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers = { 'User-Agent' : user_agent }
req = urllib.request.Request(url, headers)

htmlpage = urllib.request.urlopen(req)

print(htmlpage.read())

resu = urllib.request.urlopen('http://www.qq.com', data = None, timeout = 10)
resu.encoding="utf-8"
print(resu.read())

"""


import urllib.request
import requests
from bs4 import BeautifulSoup
 
if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = requests.get( url,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    targets_url = bf.find_all(class_='author')
    list_url = []
    for each in targets_url:
        print(str(each.get('href')))
        list_url.append(str(each.get('href')))
    print(list_url)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    