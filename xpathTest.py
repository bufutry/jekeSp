import requests
from lxml import etree
from multiprocessing import Pool


url  = "http://www.jikexueyuan.com/course/ios/?pageNum=1"

#html = requests.get(url).text

#print html
#//*[@id="2572"]/div[1]/a/img
#sele = etree.HTML(html)
#test = sele.xpath('//*[@id]/div[1]/a/img/@title')
#for i in  test:
#    print  'sss'
    #print  i

def reust(max_link):

    arr = []
    for x in range(1,max_link):
        url1  = "http://www.jikexueyuan.com/course/ios/?pageNum="+("{0}".format(x))
        arr.append(url1)
    return arr

def sider(html):
    sele = etree.HTML(html)
    test = sele.xpath('//*[@id]/div[1]/a/img/@title')
    for i in  test:
        print  i

def info(url):
    html = requests.get(url).text
    sider(html)

def min():
    pool  = Pool(processes=2)
    stt = reust(10)
    for i in  stt:
        print i
        pool.apply_async(info(i))

    pool.close()
    pool.join()

if __name__ == "__main__":
      min()
