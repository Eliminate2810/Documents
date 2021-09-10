
# codeing = utf-8

import urllib.request, urllib.error   #制定URL，获取网页数据
import urllib.parse                   #网页解析

def txtGeneral(html):
    f=open("Documents/python_crawler/file.html",'w',encoding='utf-8')
    f.write(html)
    f.close()

# #获取网页内容
# urlweb = urllib.request.urlopen("http://www.baidu.com/")
# f=open("file.txt",'w',encoding='utf-8')
# f.write(urlweb.read().decode("utf-8"))
# f.close()



# #获取一个post请求
# d = bytes(urllib.parse.urlencode({}), encoding='utf-8')             #urlencode后面必须跟一个 键值对
# response = urllib.request.urlopen("http://httpbin.org/post",data=d)        #获取post的时候，需要一个参数存储数据
# print(response.read().decode('utf-8'))



# #获取一个get请求 + 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=3)        #获取get请求 + 超时参数
#     print(response.read().decode('utf-8'))
# except Exception as e:
#     print("-"*50,"time out","-"*50)
#     print(e)



# #打开网页后，存储的数据是整个网页，可以通过各种函数看，一下举例几个
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)          #http的 状态码
# print(response.getheaders())       #获取头包信息
# print(response.getheader('Server')) #获取头包具体字典的值



#如何伪装自己是浏览器，然后访问网站
#主要是伪装headers，cookie   前者可以F12 network 查看头包信息
url = "http://www.douban.com/"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}
data = bytes(urllib.parse.urlencode({}),encoding="utf-8")       #设置解析数据参数
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")  #可以有很多参数，h和m这例可以省略
response = urllib.request.urlopen(req)      #打开网页 传入已经封装好的url
html = response.read().decode("utf-8")
txtGeneral(html)

