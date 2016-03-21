#coding:utf-8
import requests
import re
from lxml import etree

url  = "http://www.jikexueyuan.com/course/ios/?pageNum="
#hmtl =  requests.get(url)
#print hmtl.text
#href=
text1 = "httppa2dpa1dhttp href=dadada>"
pa =  re.compile(r'(?<=href=).*(?=>)',re.S)
xa = pa.findall(text1)
#print xa


class Crawler:

    fristLink = []

    def start(self):
        for y in  self.fristLink:
          print "开始处理第一个网站"
          print  y
          html1 = requests.get(y)
          self.fistInfo(html1.text)

    def fistWeb(self,pageMax):
        for x in range(1,pageMax):
          links =  url+("{0}".format(x))
          self.fristLink.append(links)

    def fistInfo(self,text):
        patter = re.compile(r"(?<= display: none;\">).*(?=</p>)",re.S)
        #print text
        math = patter.findall(text)
        print math

c = Crawler()
c.fistWeb(2)
c.start()