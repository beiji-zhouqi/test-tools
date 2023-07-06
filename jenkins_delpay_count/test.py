import requests
import datetime

def get_job_build_count(job_url):
    api_url = f'{job_url}/api/json?tree=builds[timestamp,result]'
    
    response = requests.get(api_url)
    data = response.json()

    # 统计一周内的发布次数
    count = 0
    today = datetime.date.today()
    for build in data['builds']:
        build_date = datetime.datetime.fromtimestamp(build['timestamp'] / 1000).date()
        if today - build_date <= datetime.timedelta(days=7) and build['result'] == 'SUCCESS':
            count += 1

    return count


# 统计输出7天内每个项目的发布次数，发布次数为0的不统计
url = 'https://jenkins.sz.inrobot.cloud/api/python?tree=jobs[name,url]' # 获取所有的job信息
res = requests.get(url)
for job in res.json()['jobs']:
    build_count = get_job_build_count(job_url=job['url'])
    if build_count == 0:
        pass
    else:
        print(f"一周内项目 {job['name']} 的发布次数为: {build_count}")