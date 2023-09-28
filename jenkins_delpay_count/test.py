import requests
import datetime


def exchange_date(date_string):
    d_time = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    return d_time


def get_job_build_count(start_time, end_time, job_url):
    api_url = f'{job_url}/api/json?tree=builds[timestamp,result]'
    
    response = requests.get(api_url)
    data = response.json()

    # 统计一周内的发布次数
    count = 0
    today = datetime.date.today()
    for build in data['builds']:
        build_date = datetime.datetime.fromtimestamp(build['timestamp'] / 1000).date()
        # if today - build_date <= datetime.timedelta(days=7) and build['result'] == 'SUCCESS':
        #     count += 1

        if build_date >= start_time and build_date <= end_time and build['result'] == 'SUCCESS':
            count +=1

    return count


start_time = '2023-09-18'
end_time = '2023-09-22'

# 统计输出7天内每个项目的发布次数，发布次数为0的不统计
url = 'https://jenkins.sz.inrobot.cloud/api/python?tree=jobs[name,url]' # 获取所有的job信息
res = requests.get(url)
data = []
dict = {}
parts = []
for job in res.json()['jobs']:
    build_count = get_job_build_count(exchange_date(start_time), exchange_date(end_time), job_url=job['url'])
    if build_count == 0:
        pass
    else:
        parts = job['name'].split('-', 1)
        parts.append(build_count)
        data.append(parts)
        
        
system_counts = {}

# 遍历数据列表
for item in data:
    environment, system, count = item
    
    # 检查系统名称是否已经存在于统计字典中
    if system in system_counts:
        system_counts[system][environment] = count
    else:
        system_counts[system] = {environment: count}

# 输出格式化结果
sit_count, uat_count, smzx_count = 0, 0, 0
for system, counts in system_counts.items():
    output = f"{system}:"
    for environment, count in counts.items():
        output += f" {environment}:{count}"
        if environment == 'SIT':
            sit_count = sit_count + count
        elif environment == 'UAT':
            uat_count = uat_count + count
        elif environment == 'SMZX':
            smzx_count = smzx_count + count
    print(output)
print('sit_count:{}'.format(sit_count))
print('uat_count:{}'.format(uat_count))
print('smzx_count:{}'.format(smzx_count))
        # print(f"{job['name']} 的发布次数为: {build_count}")