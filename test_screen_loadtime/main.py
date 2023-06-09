import requests
import time
import os

urls = ['https://digital-screen-sc.uat.inrobot.cloud/gltf/robot.glb', 'https://digital-screen-sc.uat.inrobot.cloud/gltf/build.glb']

def writeToFile(data):
    with open(file='./results/result.log', mode='+a', encoding='utf-8') as f:
        f.write(data)


while True:
    time_end = 1686218400
    time_now = int(time.time())
    if time_now < time_end:

        for url in urls:
            time.sleep(3)
            req = requests.get(url=url)
            take_time = req.elapsed.total_seconds()
            
            if take_time >= 1:
                writeToFile(os.system('ping digital-screen-sc.uat.inrobot.cloud'))
                # values = "请求总耗时：%s, 请求时间：%s" % (take_time, time_now)
                writeToFile(take_time, time_now)
                print("请求总耗时：%s, 请求时间：%s" % (take_time, time_now))
                writeToFile("\n-----------------------------------------\n")

    else:
        break

print('end.')