from PIL import Image
import os


def generate_image(width, height, format, target_size):
    # 创建一个新的图像对象
    image = Image.new("RGB", (width, height), "white")

    # 调整图像尺寸
    image = image.resize((width, height))

    # 调整图像保存质量，以达到目标文件大小
    image.save("temp.png", format=format, optimize=True, quality=85)  # 保存为临时文件

    # 计算生成的图片大小还差多少
    file_size = target_size - get_file_size("temp.png")

    # 生成补充文件
    generate_file(file_size)

    # 生成最终图片
    copy_img_file("ts.png")


# 生成符合大小的文件
def copy_img_file(target_image):
    # 将文件追加到图片，并生成新的图片
    commond = "copy /b"  + " temp.png" " + temp.bin " + target_image
    os.system(commond)

    print("符合条件的图片生成成功！")


# 生成指定大小文件
def generate_file(file_size):
    # 生成随机数据
    random_data = os.urandom(int(file_size))

    # 写入文件
    with open("temp.bin", "wb") as file:
        file.write(random_data)

    print("文件生成成功！")


# 获取图片大小
def get_file_size(file_path):
    import os
    return os.stat(file_path).st_size  # 返回文件大小（byte）


# 示例用法
width = 1920  # 图片宽度
height = 1080  # 图片高度
format = "png"  # 图片格式（可以是png、jpeg、bmp等）
target_size = 12  # 目标文件大小（MB）

generate_image(width, height, format, target_size * 1024 * 1024)
