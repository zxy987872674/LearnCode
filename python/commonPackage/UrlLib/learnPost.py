#!/bin/env python
#coding=utf8

#****************************************************
# Author: zhangxiangyu
# Created: 2017-10-31 15:05
# Last modified: 2017-10-31 15:05
# Filename: learnPost.py
# Description: 
#****************************************************

import  urllib
import  urllib2
  
def postFun():
    params = urllib.urlencode({'cityId':'438'})
    r = urllib2.urlopen('http://m.cyw.com/index.php?m=api&c=cookie&a=setcity', params)
    print(r.getcode(), r.msg)
    print(r.read())


if __name__ == "__main__":
    postFun()



