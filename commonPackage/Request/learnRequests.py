#!/bin/env python
#coding:utf-8

#****************************************************
# Author: zhangxiangyu
# Created: 2017-10-31 15:33
# Last modified: 2017-10-31 15:33
# Filename: learnRequests.py
# Description: 
#****************************************************
import requests

def Tget():
    r = requests.get(url='http://yuedu.baidu.com/ebook/3c0077aaa32d7375a41780bb',params={'_searchquery':'selenium-python%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4'})
    print('r.url:', r.url)
    r = requests.get('http://www.bing.com')

    print(u'HTTP状态码:', r.status_code)
    print(u'请求的url:', r.url)
    print(u'获取Headers:', r.headers)
    #print(u'响应内容:', r.text)


def Tpost():
    data = {'username':'13484545195','password':'123456'}
    r = requests.post('http://m.cyw.com/index.php?m=api&c=login&a=authorized', data=data)
    print(r.text)
    print(r.json)




if __name__ == "__main__":
    #Tget()
    Tpost()
