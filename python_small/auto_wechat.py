#引入selenium库中的 webdriver 模块
from  selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time

#自动打开微信公众号平台，然后在20s内扫码登录，自动删除重复素材图片


#打开浏览器 
try:
    #配置设置 并 启动edge浏览器
    options = EdgeOptions()
    options.use_chromium = True
    # options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = Edge(options = options)

    #打开网页最大化
    driver.get('https://mp.weixin.qq.com/')
    driver.maximize_window()
    # 等待登录
    time.sleep(20)
    #打开素材库
    driver.find_element_by_xpath('//*[@id="js_mp_sidemenu"]/div/div/ul/li[2]/ul/li[1]/ul/li[2]/a/span/span').click()
    #获取网页源码
    doc = driver.page_source
    f=open("./file.html",'w',encoding='utf-8')
    f.write(str(doc))

    # #用于获取网页内容，自动生成txt
    # c = driver.find_element_by_xpath('//*')        #account
    # f=open("./file.txt",'w',encoding='utf-8')
    # f.write(str(c))
    # f.close()
   
    # //*[@id="auto-id-1631182315532"]
    # driver.find_element_by_xpath('').click()
    



    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('big problem')      #百度搜索关键词
    # driver.find_element_by_xpath('//*[@id="su"]').click()           #点击搜索


except Exception as e:
    print("-"*50,"wrong","-"*50)
    print(e)
    print("-"*50,"wrong","-"*50)