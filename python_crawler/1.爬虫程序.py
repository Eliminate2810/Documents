# codeing = utf-8

from bs4 import BeautifulSoup              #网页解析，获取数据
import re               #正则表达式，进行文字匹配
import urllib.request, urllib.error   #制定URL，获取网页数据
import xlwt             #进行excel操作
import sqlite3          #进行sqlite数据库操作


#用于获取网页内容，自动生成txt
def txtGeneral(html):
    f=open("./file.txt",'w',encoding='utf-8')
    f.write(html)
    f.close()


#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):           #累次调用获取页面信息
        url = baseurl + str(i*25)
        html = askURL(url)          #将获取的网页信息保存到html中
        #逐一解析数据


    

    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    headers = {          #伪装浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
    }
    req = urllib.request.Request(url=url,headers=headers)  #可以有很多参数，h和m这例可以省略
    html = ""
    try:
        response = urllib.request.urlopen(req)      #打开网页 传入已经封装好的url
        html = response.read().decode("utf-8")
        txtGeneral(html)                #生成网页.txt
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
    return html    



#保存数据
def saveData(savePath):
    print("save successfully")


def main():
    baseurl="https://movie.douban.com/top250?start="
    savePath="./" 
    #爬取网页
    datalist=getData(baseurl)


    #保存数据
    # saveData(savePath)





    











#启动函数，相比于直接写，可以方便控制流程
if __name__ == "__main__":
    main()







