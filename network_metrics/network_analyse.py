log_file = './analyse_data/app.log'  # 替换为实际的日志文件路径

latency_data = []
loss_rate_data = []
with open(log_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        parts = line.split(' - ')
        timestamp = parts[0]
        level = parts[1].strip()
        message = parts[2].strip()
        
        if '平均延迟' in message:
            latency = float(message.split(':')[-1].strip())
            latency_data.append((timestamp, level, message, latency))
        elif '丢包率' in message:
            loss_rate = float(message.split(':')[-1].strip().replace('%', ''))
            loss_rate_data.append((timestamp, level, message, loss_rate))

# 按平均延迟降序排序，取前10条数据
sorted_by_latency = sorted(latency_data, key=lambda x: x[3], reverse=True)[:20]

# 按丢包率降序排序，取前10条数据
sorted_by_loss_rate = sorted(loss_rate_data, key=lambda x: x[3], reverse=True)[:20]

# 打印平均延迟最高的10条数据
print('平均延迟最高的20条数据：')
for item in sorted_by_latency:
    print(f'Timestamp: {item[0]}, Level: {item[1]}, Message: {item[2]}, Latency: {item[3]}')

# 打印丢包率最高的10条数据
print('丢包率最高的20条数据：')
for item in sorted_by_loss_rate:
    print(f'Timestamp: {item[0]}, Level: {item[1]}, Message: {item[2]}, Loss Rate: {item[3]}')
