#-*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib



##访问网站的时候输出错误方式一

# request=urllib2.Request("http://127.0.0.1:8080/666.gsp")
# 
# urllib2.socket.setdefaulttimeout(1) # 另一种方式
# 
# try:
#     content=urllib2.urlopen(request)
#     #print content.read()
# except urllib2.HTTPError, e:
#     e.code
#     e.reason
# else:
#     print("OK");



##访问网站的时候输出错误方式二
# urllib2.socket.setdefaulttimeout(3) # 另一种方式
# 
# requset = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(requset)
#     print("ok")
# except urllib2.URLError, e:
#     print e.reason
#     print("og")



#访问网站的时候获取cookie并且设置cookie

# cookie=cookielib.CookieJar()  #实力化cookie
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)#设置打开的时候，获取cookie
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('https://www.baidu.com')#这一步的时候，其实就是已经给cookie赋值啦
# 
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value
#     
# 
# #设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# response = opener.open("https://www.baidu.com")
# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)







#实际登录到百度网站
# filename = 'qq_email.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#             'account':'15200857729',
#             'password':'wbc120732'
#         })
# #登录教务系统的URL
# loginUrl = 'http://www.zhihu.com/#signin'
# #模拟登录，并把cookie保存到变量
# try:
#     result = opener.open(loginUrl,postdata)
#     #打印登陆的情况
#     print result.read()
# except urllib2.HTTPError, e:
#     e.code 
# #保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://en.mail.qq.com/cgi-bin/frame_html?sid=ZtiJzZWUp1HKRANU&r=b5c5b876a9976fef1975556dc393f155'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()







###政策表达式
# -*- coding: utf-8 -*-

#导入re模块
import re
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')
# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hel lo CQC!')
#如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'
#如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'
#如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！'
#如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'
    

#一个简单的match实例
 
import re
# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
 
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3') ##调换他们之间的顺序





import re

pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')


pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print re.sub(pattern,r'\2 \1', s)
 
temp=0

def func(m):
    global temp
    #temp=temp+1   #如果这么写会使python编译器产生误解，temp是局部变量的
    temp+=1
    print temp
    return m.group(1).title() + 'gg' + m.group(2).title()
 
print re.sub(pattern,func, s)





   