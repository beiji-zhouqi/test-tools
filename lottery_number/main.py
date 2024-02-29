import tkinter as tk
import random


def generate_random_number():
    number = random.randint(1, 100)
    result_label.config(text=str(number))


root = tk.Tk()
root.title("抽奖随机数字")

# 设置窗口大小和位置
root.geometry("800x600")

generate_button = tk.Button(root, text="抽奖", command=generate_random_number)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
