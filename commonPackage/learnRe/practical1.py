#coding:utf-8

import re
from configobj import ConfigObj
import os

PATH = os.path.abspath(os.curdir)
route_info = ConfigObj(PATH + "/resources/routeCenter.data")

def getRoute(head,content):
    route = route_info[head][content]
    print route
    return route

def getTheoryWeight(head,content):
    theoryweight = route_info[head][content]
    print theoryweight
    return theoryweight

def getTestWeight(r):
    path = './a.txt'
    routeinfoFile = open(path,'r')
    fileread = routeinfoFile.read()
    routeinfoFile.close()
    print re.search(r,fileread)
    try:
	weightData = re.search(r,fileread).group(1)
	print weightData
	return weightData
    except Exception,ex:  
        print Exception,":",ex

def checkWeight(head,rContent,wContent):
    testWeight = getTestWeight(getRoute(head,rContent))
    theoryweight = getTheoryWeight(head,wContent)
    if testWeight == theoryweight:
        print 'pass!'
        pass
    else:
        error_message = ' weight is not equal to theoryweight data ! '
        raise AssertionError(error_message, 'testWeight:', testWeight,'theoryweight:', theoryweight) 





if __name__ == "__main__":
    route = getRoute('route_info_3222019585','routeInfo_2')
    getTheoryWeight('route_info_3222019585','weight_2')
    getTestWeight(route)
    checkWeight('route_info_3222019585','routeInfo_2','weight_2')
    
