#列表  元组  字典  集合



#字典的定义
info={"name":"张三","age":18}

#字典的访问
print(info["name"])
print(info["age"])

#直接使用info访问不存在的键会报错
print(info.get("gender"))       #使用get没有，则返回none
print(info.get("gender","m"))       #get可以设定返回值

