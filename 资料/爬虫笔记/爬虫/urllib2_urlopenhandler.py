#coding:utf-8

import urllib2


#构建一个httphandler处理器对象，支持处理一个http请求
#http_handler = urllib2.HTTPHandler()

#在httphandler中增加参数“debuglevel=1"将会自动打开debug log模式，
#程序在执行的时候会打印收发包的信息

http_handler = urllib2.HTTPHandler(debuglevel=1)
#调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)

#print response.read()

