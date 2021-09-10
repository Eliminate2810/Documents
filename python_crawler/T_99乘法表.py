
'''
#                99乘法表双for版
for i in range(1,10):
    for j in range (1,10):
        a=i*j
        print("%d*%d=%d"%(i,j,a),end=" ")
        if i==j:
            print("\n")
            break
'''


#              99乘法表while版
i=1
j=1
while (i!=10):
    a=i*j
    print("%d*%d=%d"%(i,j,a),end=" ")
    if i==j:
        print("\n")
        i+=1
        j=1
    else:
        j+=1

