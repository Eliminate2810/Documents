#引入selenium库中的 webdriver 模块
from  selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time

# 自动输入激活码测试
def auto_arouse():
    

    driver.find_element_by_xpath('//*[@id="app"]/nav/a[3]').click()  #点击兑换码激活
    f=open("./file.txt",'r',encoding='utf-8')
    for i in range(2):
        c = f.readline()
        time.sleep(1)
        driver.find_element_by_class('code').send_keys(c)      #输入兑换码
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/button').click()  #点击兑换 
        # <input placeholder="请输入您的激活码" class="code">
        #等待响应
        time.sleep(1)
        #第一次有条款需要同意
        if i==0:
            driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[2]').click() #点击同意
        # driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/div[3]').text()    #获取返回激活结果
        time.sleep(2)
        
    f.close()


#打开浏览器 
try:
    #配置设置 并 启动edge浏览器
    options = EdgeOptions()
    options.use_chromium = True
    # options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = Edge(options = options)

    #打开网页并最大化窗口
    driver.get('https://www.yjwujian.cn/account/#/welcome')
    driver.maximize_window()
    #登录
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').click()           #点击搜索
    time.sleep(15)

    #自动激活
    auto_arouse()

   
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
 



