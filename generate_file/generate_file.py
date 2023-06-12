import os


def generate_file(file_size, file_type):
    # 转换文件为bytes
    target_size = file_size * 1024 * 1024

    # 生成随机数据
    random_data = os.urandom(int(target_size))

    # 写入文件
    with open("generated_file" + file_type, "wb") as file:
        file.write(random_data)

    print("File generated successfully!")


file_size = 10  # Target file size in MB
file_type = ".doc"
generate_file(file_size, file_type)
