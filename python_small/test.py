#引入selenium库中的 webdriver 模块
from  selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time

#打开浏览器 
try:
    #配置设置 并 启动edge浏览器
    options = EdgeOptions()
    options.use_chromium = True
    # options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = Edge(options = options)

    #打开网页
    driver.get('https://www.yjwujian.cn/account/#/welcome')
    #登录
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').click()           #点击搜索
    time.sleep(5)

    #用于获取网页内容，自动生成txt
    c = driver.find_element_by_xpath('//*')        #account
    f=open("./file.txt",'w',encoding='utf-8')
    f.write(str(c))
    f.close()
   
    # //*[@id="auto-id-1631182315532"]
    # //*[@id="auto-id-1631182167517"]
    # driver.find_element_by_xpath('').click()
    # driver.find_element_by_xpath('').click()
    



    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('big problem')      #百度搜索关键词
    # driver.find_element_by_xpath('//*[@id="su"]').click()           #点击搜索


except Exception as e:
    print("-"*50,"wrong","-"*50)
    print(e)
    print("-"*50,"wrong","-"*50)
 



