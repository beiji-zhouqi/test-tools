import subprocess
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import socket
import time
import threading
 
 
hp = Tk()#创造窗口对象
hp.title("手动网络检测器")#标题
w = hp.winfo_screenwidth()#获取屏幕宽度
h = hp.winfo_screenheight()#获取屏幕高度
width = 370
height = 325
pw = (w - width - 100)/2
ph = (h - height - 130)/2
hp.geometry("%dx%d+%d+%d"%(width,height,pw,ph))#设置窗口长度和宽度
 
hp.resizable(False,False)#设置窗口不可改变长度和宽度
 
global 加强检测是否
加强检测是否 = False
 
data = []
 
 
def 加强():
    global 加强检测是否
    
    try:
        if 加强检测是否 == False:#加强检测是否为"否"
            加强检测是否 = True
            
        elif 加强检测是否 == True:#加强检测是否为"是"
            加强检测是否 = False
            
        else:
            pass
    except:
        tk.messagebox.showinfo("","ERROR")#(错误)
        
##加强模式确认
        
 
def 开始检测(normal_bag = 1,strengthen_bag = 2,normal_size = 64,strengthen_size = 256):
    while True:#默认循环
        时间 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))#获取当前时间
        ip = 输入.get()#获取ip地址
        data.append(ip)#获取ip写入数据列表
        newdata = list(set(data))#列表去重
        输入["value"] = newdata#输入框获取新ip列表
 
        if ip == "":
            tk.messagebox.showinfo("","输入不可为空")
            break
            #当输入框内容为空时,弹出为空提示,退出循环
            
        while True:
            if 加强检测是否 == False:
                检测 = subprocess.Popen("ping -w 1 -n %d -l %d %s"%(normal_bag,normal_size,ip),stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True)
                break
                #正常检测
            if 加强检测是否 == True:
                检测 = subprocess.Popen("ping -w 1 -n %d -l %d %s"%(strengthen_bag,strengthen_size,ip),stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True)
                break
                #加强检测
            #使用subprocess库,调用命令指示符指令(ping)检查网络连通性
                        
        out,err = 检测.communicate()#读取子线程数据
        
        if 检测.returncode == 0:#返回状态码正常
            tk.messagebox.showinfo(message = "网络连接正常")
            状态栏.insert(END,时间)
            状态栏.insert(END," 网络连接正常\n")
            状态栏.see(END)
            break   
            #连接正常
                    
        else:
            tk.messagebox.showinfo(message = "连接错误")
            状态栏.insert(END,时间)
            状态栏.insert(END," 网络连接错误\n")
            状态栏.see(END)
            break   
            #连接错误
 
 
##开始检测
          
def 自动获取ip():
    host = socket.gethostname()#获取本机主机名
    ip = socket.gethostbyname(host)#获取当前电脑ip地址
    输入.insert(END,ip)#写入输入框
    #自动获取ip
 
def 清空输入框():
    输入.delete(0,END)#清空输入框内容
    清空.deselect()#恢复清空选择框状态
    #清空输入框
 
框架 = Canvas()
框架.create_rectangle(5,10,300,266)
框架.place(x = 30,y = 20)
标签 = ttk.Label(hp,text = "Instrument",font = ("Arial",13))
标签.place(x = 130,y = 19)
输入 = ttk.Combobox(hp)
输入.place(x = 50,y = 60,width = 110,height = 23)
开始检测 = ttk.Button(hp,text = "检测",command = 开始检测)
开始检测.place(x = 170,y = 58,width = 50,height = 29)
加强检测 = tk.Checkbutton(hp,text = "加强检测",command = 加强)
加强检测.place(x = 200,y = 95)
自动获取 = ttk.Button(hp,text = "自动获取ip",command = 自动获取ip)
自动获取.place(x = 228,y = 58,width = 78,height = 30)
清空 = tk.Checkbutton(hp,text = "清空输入内容",command = 清空输入框)
清空.place(x = 200,y = 120)
提示 = ttk.Label(hp,text = "Tip:请输入正确的ip地址",font = ("Arial",10))
提示.place(x = 44,y = 92)
状态栏 = Text(hp,bg = "black",fg = "white",relief = RAISED)
状态栏.place(x = 50,y = 151,width = 245,height =122)
滚动条 = ttk.Scrollbar(hp)
滚动条.config(command = 状态栏.yview)
状态栏.config(yscrollcommand = 滚动条.set)
滚动条.place(x = 295,y = 151,height = 122)
 
##tk组件设置
 
if __name__ == "__main__":
    hp.mainloop()#主事件循环运行