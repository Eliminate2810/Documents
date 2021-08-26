# password=input("请输入密码")
# print("您刚才输入的密码是：",password)


alist=["abc",123,'ac']
blist=["bbb",321,"bc"]


#添加
alist.append('end')     #末尾添加元素end

alist.extend(blist)     #末尾添加列表blist

alist.insert(1,"b")     #在alist下表为1的元素后面添加“b”


#删除
del alist[2]            #删除列表下标位置元素

alist.pop()             #删除末尾元素

alist.remove("ac")      #直接删除找到的第一个具体元素


#改
alist[2]="xiabiao"


#查找：if语句
findname=input("输入要查找的信息")
if findname in alist:
    print("找到了对应的信息")
else:
    print("没找着")

a=["a","b","c","d","e","f"]
a.index("e",1,5)        #查找元素，起始查找下标，最终查找下标     返回找到的下标值
                        #查找范围左闭右开       [1,5)

a.count("a")            #查找某个元素出现次数

a.sort(reverse=True)    #降序



