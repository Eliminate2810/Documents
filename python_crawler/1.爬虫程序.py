# codeing = utf-8

from bs4 import BeautifulSoup              #网页解析，获取数据
import re               #正则表达式，进行文字匹配
import urllib.request, urllib.error   #制定URL，获取网页数据
import xlwt             #进行excel操作
import sqlite3          #进行sqlite数据库操作

#影片链接规则
findLink = re.compile(r'<a href="(.*?)">')      #创建正则对象（字符串模式）
#影片图片
findImg = re.compile(r'<img.*src="(.*?)"',re.S)     #re.S包括换行符
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到评价
findInq = re.compile(r'<span class="inq">(.*)</span>')
#导演等相关内容
findBD = re.compile(r'<p class="">(.*?)</p>',re.S)



#用于获取网页内容，自动生成txt
def txtGeneral(html,rank):
    f=open("./file%d.html"%rank,'w',encoding='utf-8')
    f.write(html)
    f.close()


#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,1):           #累次调用获取页面信息  (0,10)
        url = baseurl + str(i*25)      #豆瓣×25，猫眼×10
        html = askURL(url)          #将获取的网页信息保存到html中
        # txtGeneral(html,i)          #测试网页获取正常，输出文件file%i.html
        
        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all(r'div',class_=r'item'):
            data = []         #用于保存电影信息
            item = str(item)        #转化为字符串，用正则搜索

            #影片链接
            link = re.findall(findLink,item)[0]     #正则搜索，从item中搜索findlink(globe)
            data.append(link)                       #添加链接
            imgsrc = re.findall(findImg,item)[0]    
            data.append(imgsrc)                     #添加图片
            titles = re.findall(findTitle,item)[0]  #如果要去掉字符，可以用s.replace("/","")
            data.append(titles)                     #添加标题
            rating = re.findall(findRating,item)[0]
            data.append(rating)                     #添加评分
            judge = re.findall(findJudge,item)[0]
            data.append(judge)                      #添加评价人数
            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq=inq[0].replace("。","")
                data.append(inq)                    #添加评价语
            else:  
                data.append(" ")                    #留空
            
# #------------------------------不懂的地方-----------------------------           
#             bd = re.findall(findBD,item)
#             bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br/>
#             bd = re.sub('/'," ",bd)                 #去掉/
#             data.append(bd.strip())                 #去掉空格
# #------------------------------不懂的地方----------------------------- 

            datalist.append(data)       #输出
    return datalist


#得到指定一个URL的网页内容      返回一个 html
def askURL(url):
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
        # txtGeneral(html)                #生成网页.txt
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
    baseurl="https://movie.douban.com/top250?start="        #25一页     豆瓣
    # baseurl="https://maoyan.com/board/4?offset="            #10一页     猫眼
    savePath="./" 
    #爬取网页
    datalist=getData(baseurl)

    # f=open("./datafile.txt",'w',encoding='utf-8')     #测试
    # for i in range(len(datalist)):
    #     f.write(str(datalist[i])+"\n")
    # f.close()

    #保存数据
    # saveData(savePath)





    











#启动函数，相比于直接写，可以方便控制流程
if __name__ == "__main__":
    main()







