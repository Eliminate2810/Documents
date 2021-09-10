#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import random
import string

f=open("./file.txt",'w',encoding='utf-8')
for i in range(50):
    seed = "1234567890abcdefghijklmnopqrstuvwxyz"  #ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    f.write("aa"+str(salt)+"\n")
f.close()

# #第二种方法
 
# salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
# print salt

