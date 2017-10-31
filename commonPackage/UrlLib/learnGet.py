#!/bin/env python
#coding=utf8

#****************************************************
# Author: zhangxiangyu
# Created: 2017-10-31 14:13
# Last modified: 2017-10-31 14:13
# Filename: learnGet.py
# Description: 
#****************************************************

import urllib
import urllib2

def getBaidu():
    r = urllib2.urlopen('http://www.baidu.com')
    print('Response code:', r.getcode(), r.msg)
    print('headers:', dir(r.headers))
    #print('read:', r.read())


if __name__ == "__main__":
    getBaidu()
