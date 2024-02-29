import tkinter as tk
import tkinter.messagebox


# 调用TK，设置标题
root = tk.Tk()
# 设置标题
root.title("设置一个标题")
# 设置分辨率
root.geometry("800x600")
# 设置icon
root.iconbitmap("C:/Users/zhouqi1/Pictures/favicon.ico")
# 设置窗口背景颜色
root["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text = tk.Label(root, text="C语言中文网，欢迎您", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()

# # 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
# button = tk.Button(root, text="关闭", command=root.quit)
# # 将按钮放置在主窗口内
# button.pack(side="bottom")


#################################################################################
# 创建一个执行函数，点击下拉菜单中命令时执行
def menuCommand(arg=None):
    tkinter.messagebox.showinfo("下拉菜单", "您正在使用下拉菜单功能")


def func(arg=None):
    print('您通过弹窗菜单执行了命令.')


# 菜单
main_menu = tk.Menu(root)

# 文件菜单
filemenu = tk.Menu(main_menu, tearoff=False)


# 新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
filemenu.add_command(label="新建", command=menuCommand, accelerator="Ctrl+N")
filemenu.add_command(label="打开", command=menuCommand, accelerator="Ctrl+O")
filemenu.add_command(label="保存", command=menuCommand, accelerator="Ctrl+S")
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)

# 在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
main_menu.add_cascade(label="文件", menu=filemenu)

# 新增命令菜单项，使用 add_command() 实现
main_menu.add_command(label="文件")
main_menu.add_command(label="编辑")
main_menu.add_command(label="格式")
main_menu.add_command(label="查看")
main_menu.add_command(label="帮助")

# 显示菜单
root.config(menu=main_menu)
# 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
root.bind("<Control-n>", menuCommand)
root.bind("<Control-N>", menuCommand)
root.bind("<Control-o>", menuCommand)
root.bind("<Control-O>", menuCommand)
root.bind("<Control-s>", menuCommand)
root.bind("<Control-S>", menuCommand)


# 定义事件函数
def command(event):
    main_menu.post(event.x_root, event.y_root)


root.bind("<Button-3>", command)

# 开启主窗口
root.mainloop()
