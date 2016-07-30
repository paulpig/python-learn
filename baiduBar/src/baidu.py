# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()
    

class BAIDUBAR:
    #构造函数，初始化
    def __init__(self):
        self.page_number=0
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.floorOwner=False
        self.contentOfTitle=None
        self.contentOfAutor=[]
        self.contentOfLou=[]
        self.contentOfContent=[]
    
        #网站中获取网页内容
    #para0:网站页数
    #return：html
    def captureHTML(self,pageIndex):
        try:
            if self.floorOwner==True:
                url = 'http://tieba.baidu.com/p/4459923108?see_lz=1&pn=' + str(pageIndex)
            else:
                url = 'http://tieba.baidu.com/p/4459923108?pn=' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url,headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read()
            
            #将获取网站写入到文件中
            file_object = open('/home/wubingchao/workspace/baiduBar/src/thefile.html', 'w')
            file_object.write(pageCode)
            file_object.close( )
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"获取网站数据失败,错误原因",e.reason
                return None
    
    
    #获取html转化为自己需要的内容（正则表达式） 
    #return: content
    def ConvertToContent(self,pagenumber):
        content = self.captureHTML(pagenumber);
        if not content:
            print "htmlcontent wrong!!!"
            #return None
        #获取帖子标题
        self.contentOfTitle=self.getTitle(content)
        #获取帖子的作者
        self.contentOfAutor.append(self.getAutor(content))
        #获取帖子的楼数
        self.contentOfLou.append(self.getLouNum(content))
        #获取帖子的内容
        self.contentOfContent.append(self.getContent(content))
    
    
    
    #获取帖子的标题
    def getTitle(self,content):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,content)
        if result:
            #print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            print "gettitle wrong"
            return None
     
    
    #获取帖子的作者
    def getAutor(self,content):
        pattern = re.compile('<a data-field=.*?alog-group=.*?target="_blank">(.*?)</a>',re.S)
        result = re.findall(pattern,content)
        if result:
            returnResult=[]
            for item in result:
                returnResult.append(Tool().replace(item))
            return returnResult
        else:
            print "getautor wrong"
            return None
        
    
    #获取帖子的楼数
    def getLouNum(self,content):
        pattern = re.compile('</a></span><span class="tail-info">(.*?)楼</span>',re.S)
        result = re.findall(pattern,content)
        if result:
            returnResult=[]
            for item in result:
                returnResult.append(Tool().replace(item))
            return returnResult
        else:
            print "getlounum wrong"
            return None  
        
    
    #获取帖子的内容
    def getContent(self,content):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        result = re.findall(pattern,content)
        if result:
            returnResult=[]
            for item in result:
                returnResult.append(Tool().replace(item))
            return returnResult
        else:
            print "getcontentwrong"
            return None      
        
    #输出信息
    def printMyContent(self,numofcontent,numofpage):
        print "标题:"
        print self.contentOfTitle
        print "用户："
        print self.contentOfAutor[numofpage][numofcontent]    
        print "楼层："
        print self.contentOfLou[numofpage][numofcontent]    
        print "内容："
        print self.contentOfContent[numofpage][numofcontent]              
        return None
    
        #启动类
    def start(self):
        numOfContent=0
        while (raw_input() != "q"):
            if self.page_number==0:
                self.ConvertToContent(self.page_number)
            if len(self.contentOfLou[self.page_number])<1:
                self.page_number+=1
                self.ConvertToContent(self.page_number)
            
            self.printMyContent(numOfContent,self.page_number)
            numOfContent+=1
        return None 


print "hello world"
baidu=BAIDUBAR()
baidu.start()
   