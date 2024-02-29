import http.client
import json

conn = http.client.HTTPSConnection("chyvpn.cyou")

headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua-mobile': "?0",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41",
    'sec-ch-ua-platform': '"Windows"',
    'origin': "https://chyvpn.cyou",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://chyvpn.cyou/user",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    'Cookie': "PHPSESSID=g2m6i25h607hkfqa7gddldpjel; crisp-client/session/7850791f-bbe4-4874-9f05-c9dea3c63595=session_c09e3ab5-2942-4ecd-b78a-8668314981c9; crisp-client/session/7850791f-bbe4-4874-9f05-c9dea3c63595/63b7fad5-1dec-36d6-9233-aad12f2e9949=session_c09e3ab5-2942-4ecd-b78a-8668314981c9; uid=13358; email=beiji.zhouqi@gmail.com; key=178363fcff57bf149f4bebfb1cc8acaea8b246db337fd; ip=12cfafd20de1f8e7273f2cf923360dad; expire_in=1706669365; crisp-client/session/e6a568ae-d37b-4f8a-a3d3-8dc92732b3f4=session_75c4a71d-5d49-4fcc-aea9-72d98b5e2d81; crisp-client/session/e6a568ae-d37b-4f8a-a3d3-8dc92732b3f4/63b7fad5-1dec-36d6-9233-aad12f2e9949=session_75c4a71d-5d49-4fcc-aea9-72d98b5e2d81"
    }

conn.request("POST", "/user/checkin", headers=headers)

res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")
json_data = json.loads(data)
print(json_data)

from datetime import datetime


with open('out.log', 'a+') as file:
    file.write(f"{datetime.now().strftime('%Y%m%d')}" + ' ' + str(json_data))
