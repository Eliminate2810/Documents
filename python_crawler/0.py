# codeing = utf-8

from bs4 import BeautifulSoup              #网页解析，获取数据
import re               #正则表达式，进行文字匹配
import urllib.request, urllib.error   #制定URL，获取网页数据
import xlwt             #进行excel操作
import sqlite3          #进行sqlite数据库操作



def main():
    baseurl="https://www.deepl.com/"
    url = baseurl
    headers = {          #伪装浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.8031 SLBChan/11",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }
    req = urllib.request.Request(url=url,headers=headers)  #可以有很多参数，h和m这例可以省略
    html = ""
    try:
        response = urllib.request.urlopen(req)      #打开网页 传入已经封装好的url
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html,"html.parser")
        # soup.find_all(r'div',class_=r'item')

        f = open("./printfile/blank.html","w",encoding="utf-8")
        f.write(str(soup))
        f.close()
        
    except Exception as e:          #返回错误信息
        print("-"*50,"wrong","-"*50)
        print(e)
        print("-"*50,"wrong","-"*50)
        if hasattr(e,"code"):
            print(e.code)
            print("-"*50,"wrong","-"*50)
        if hasattr(e,"reason"):
            print(e.reason)
            print("-"*50,"wrong","-"*50)


if __name__ == "__main__":
    main()
