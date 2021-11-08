def auto_arouse():

    f=open("./file.txt",'r',encoding='utf-8')
    for i in range(10):
        c = f.readline()
        print(c,end="")
    f.close()

auto_arouse()
