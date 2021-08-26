
global content

def read():           #获取内容
    global content
    f=open("Documents/python_crawler/gushi.txt",'r',encoding='utf-8')
    content=f.read()
    f.close()
def copy():           #复制
    f=open("Documents/python_crawler/copy.txt",'w',encoding='utf-8')
    f.write(content)
    f.close()
    print("复制完毕")


f=open("Documents/python_crawler/gushi.txt",'w',encoding='utf-8')
f.write('''《关雎》
关关雎鸠，在河之洲。
窈窕淑女，君子好逑。
参差荇菜，左右流之。
窈窕淑女，寤寐求之。
求之不得，寤寐思服。
悠哉悠哉，辗转反侧。
参差荇菜，左右采之。
窈窕淑女，琴瑟友之。
参差荇菜，左右芼之。
窈窕淑女，钟鼓乐之。''')
f.close()

read()
copy()
