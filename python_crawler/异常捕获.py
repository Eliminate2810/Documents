

#捕获所有的异常并且反馈为字符串形式的错误信息
try:
    f=open("test.txt","r")
    print(num)
except Exception as result:
    print("-"*15,"有错误","-"*15)
    print(result)
    print("-"*15,"有错误","-"*15)
    if hasattr(result,"code"):
        print(result.code)
    if hasattr(result,"reason"):
        print(result.reason)

finally:
    #用于即使有错误也要强制执行的语句
    print()
