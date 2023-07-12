import subprocess
import platform
import time
import re
import logging
import os


# 配置日志记录器
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 判断当前系统
def check_platform():
    current_os = platform.system()

    return current_os

# 当文件大于1M时，只保留最新1000条数据
def process_large_file(file_path):
    # 获取文件大小（以字节为单位）
    file_size = os.path.getsize(file_path)

    if file_size > 1 * 1024 * 1024:  # 判断文件大小是否大于1MB
        # 读取文件的每一行数据
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 获取要保留的最后1000条数据
        last_1000_lines = lines[-1000:]

        # 写入保留的最后1000条数据到新文件
        with open(file_path, 'w') as file:
            file.writelines(last_1000_lines)

        logging.info("文件已处理，保留最后1000条数据")
        # print("文件已处理，保留最后1000条数据")
    else:
        logging.info("文件大小未超过1MB，无需处理")
        # print("文件大小未超过1MB，无需处理")

def check_latency(host):

    if check_platform() == 'Windows':
        # 执行ping命令来测试延迟
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        # 在列表中查找包含"Average"的字符串
        lines = output.decode().split('\n')
        average_str = [s for s in lines if "Average" in s]

        # 提取"Average"数值
        if average_str:
            average_value = average_str[0].split("=")[-1].strip()
            # print("平均延迟:", average_value)
            logging.info(f'平均延迟: {average_value}')

    if check_platform() == 'Linux':
        # 执行ping命令来测试延迟
        process = subprocess.Popen(['ping', '-c', '4', host], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        # 解析ping命令的输出，提取平均延迟信息
        lines = output.decode().split('\n')
        for line in lines:
            if line.startswith('rtt'):
                average_value = line.split('=')[1].split('/')[1].strip()
                # print('平均延迟:', average_value)
                logging.info(f'平均延迟: {average_value}')

def check_packet_loss(host):
    if check_platform() == 'Windows':
        # 执行ping命令来测试延迟
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        # 在列表中查找包含"Average"的字符串
        lines = output.decode().split('\n')
        packet_loss = [s for s in lines if "loss" in s]

        # 提取"Average"数值
        if packet_loss:
            packet_loss = packet_loss[0].split("=")[-1].strip()
            match = re.search(r'\d+', packet_loss)
            if match:
                packet_loss = match.group()
                # print("丢包率:", packet_loss)
                logging.info(f'丢包率: {packet_loss}')

    if check_platform() == 'Linux':
        # 执行ping命令来测试延迟
        process = subprocess.Popen(['ping', '-c', '4', host], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        # 解析ping命令的输出，提取丢包率信息
        lines = output.decode().split('\n')
        for line in lines:
            parts = line.split(",")
            for part in parts:
                if "包丢失" in part or "packet loss" in part:
                    packet_loss = part.split()[0]
                    # print(packet_loss)
                    logging.info(f'丢包率: {packet_loss}')


# 设置定时任务的时间间隔（秒）
check_interval = 10
host = '134.175.136.198'

# 无限循环执行定时任务
while True:
    # 检测延迟
    check_latency(host)

    # 检测丢包率
    check_packet_loss(host)

    # 检测文件大小
    process_large_file('app.log')

    time.sleep(check_interval)


