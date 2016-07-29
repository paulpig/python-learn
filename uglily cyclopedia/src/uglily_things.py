# -*- coding:utf-8 -*-


###构建正则表达式是这个的关键点。.*?  表示非贪婪的任意匹配    (.*?) 将匹配的结果放入元祖中   
###最后items的结构是列表中有元组
###有些网站需要设置headers，服务器需要知道如何解析request的数据包。
###编码问题有事也得注意
import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page) #str 转换为string类型
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
#     print response.read()
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[1],item[2]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        

