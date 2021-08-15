import tkinter as tk


root=tk.Tk()
root.geometry('1200x675+150+100')#窗口大小
#root.resizable(False, False)


#b1,b2,b3分别实现播放，暂停，导入视频功能
b1=tk.Button(root, text='播放', font=('Arial', 12), activeforeground='red')
b2=tk.Button(root, text='暂停', font=('Arial', 12), activeforeground='red' )
b3=tk.Button(root, text="导入视频", font=('Arial', 12), activeforeground='red')


b3.place(relx=0.9, rely=0.9, relwidth=0.1, relheight=0.1)
b2.place(relx=0.9, rely=0.8, relwidth=0.1, relheight=0.1)
b1.place(relx=0.9, rely=0.7, relwidth=0.1, relheight=0.1)

tk.mainloop()