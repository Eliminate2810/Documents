import tkinter as tk
 
root = tk.Tk()
root.geometry('1150x950+150+100')
root.title('检测J波界面化')
#root.resizable(False, False)
#设置条形框
photo = tk.PhotoImage(file="C:\\Users\\96472\\Pictures\\Saved Pictures\\图片1.png") 
Lab= tk.Label(root,text='欢迎使用J波检测',compound='center',font = ('微软雅黑',30),image= photo)
Lab.pack()#设置主界面
   
def new_window():
    window1 = tk.Toplevel(root)
    window1.geometry('650x450+150+100')
    lab1 = tk.Label(window1,text='hello')
    lab1.pack()
 
but = tk.Button(root,text='进入',bg = 'green',command=new_window) #传递
but.pack(side="right")
 
root.mainloop()    
 