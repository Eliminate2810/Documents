# codeing = utf-8

from bs4 import BeautifulSoup              #网页解析，获取数据
#能将复杂的html文档转化为一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种
# - Tag
# - Navigablestring
# - BeautifulSoup
# - Comment

file = open("./Documents/python_crawler/file.html", "rb")
html = file.read()

# #1.得到html中标签tag信息
bs = BeautifulSoup(html,"html.parser")          
# print(bs.title)         #<title>豆瓣</title>
# print(bs.title.string)      #  豆瓣

# #2.获取字符串信息NavigableString
# print(bs.a.attrs)            #获取a结构下面的字典

# #3.BeautifulSoup 整个文档信息
# print(bs)  

# #4.Comment  是一个特殊的字符串的注释
# print(bs.a.string)


#文档的遍历
# print(bs.head.contents)     #各种子节点，兄弟节点等等，树结构



#文档的搜索

# #1.find_all()           全部匹配才显示
# t_list = bs.find_all("a")
# print(t_list)

# #2.正则表达式搜索：使用search()方法匹配内容     最常用
# import re
# t_list = bs.find_all(re.compile("a"))   #标签Tag包含a，则显示       正则表达式显示
# print(t_list)

# #3.传入一个函数，根据函数要求搜索           了解，难
# def name_is_existing(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_existing)

# #4.kwargs 传入参数搜索        常用参数text={""}
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# # 5.limit 限制个数
# t_list = bs.find_all("a",limit=3)       #只找3个

# #6.css选择器
# t_list = bs.select("title")     #通过标签查找
# t_list = bs.select(".info")     #通过类名查找
# t_list = bs.select("#u1")       #通过id查找
# t_list = bs.select("a[class='datetime']")       #通过属性查找
# t_list = bs.select("head > title")              #通过子标签查找
# t_list = bs.select(".info ~ title")             #通过兄弟节点查找       只找info的兄弟节点为title的
# print(t_list[0].gete_text())


