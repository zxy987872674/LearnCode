#!/bin/env python
#coding=utf8

#****************************************************
# Author: zhangxiangyu
# Created: 2017-10-31 11:11
# Last modified: 2017-10-31 11:11
# Filename: learnGet.py
# Description: 
#****************************************************

import httplib

def getBaidu():
    http_client = httplib.HTTPConnection('baidu.com', 80, timeout=20)
    http_client.request('GET','')
    r = http_client.getresponse()
    print dir(r)
    print u'请求状态码:\n', r.status
    print u'请求是否ok:\n', r.reason
    print u'请求头:\n', r.getheaders()
    print u'Response消息结构:\n', r.msg
    print u'响应内容:\n', r.read() 



if __name__ == "__main__":
    getBaidu()

