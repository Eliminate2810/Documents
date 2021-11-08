#引入selenium库中的 webdriver 模块
from  selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time

#配置设置 并 启动edge浏览器
options = EdgeOptions()
options.use_chromium = True
# options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
driver = Edge(options = options)

#打开网页最大化
driver.get('https://www.baidu.com/')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('big problem')      #百度搜索关键词
# kw_find = driver.find_element_by_id('kw')
#kw_find= driver.find_element_by_class_name('s_ipt')
#kw_find= driver.find_element_by_name('wd')
#kw_find = driver.find_element_by_xpath('//*[@id="kw"]')
#kw_find = driver.find_element_by_css_selector('#kw') #id用#kw，class用.s_ipt ，与css的简写方式相同



driver.find_element_by_xpath('//*[@id="su"]').click()           #点击搜索
time.sleep(3)       #等待响应3S

