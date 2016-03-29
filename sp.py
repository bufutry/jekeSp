#coding:utf-8
import requests
import re

url  = "http://www.jikexueyuan.com/course/ios/?pageNum="

class Crawler:

    fristLink = []
    datsour = []

    def start(self):
        for y in  self.fristLink:
          print "开始处理网站"
          print  y
          html1 = requests.get(y)
          self.fistInfo(html1.text)

    def fistWeb(self,pageMax):
        for x in range(1,pageMax):
          links =  url+("{0}".format(x))
          self.fristLink.append(links)

    def fistInfo(self,text):
        tmp = []
        patter = re.compile(r'<!--list-->.*<div id="page-nav"></div>?',re.S)
        math = patter.findall(text)
        pater1 = re.compile(r'<img src=[^>]*',re.S)
        for x in  pater1.findall(math[0]):
            title = re.search('title="(.*)" alt',x,re.S).group(1)
            tmp.append(title)
            print re.search('title="(.*)" alt',x,re.S).group(1)

c = Crawler()
c.fistWeb(10)
c.start()