# # import requests module 
# import requests 

# # Making a get request 
# # response = requests.get('https://baidu.com') 

# url = "http://10.55.16.171:7861/chat/chat"
# data = {"query": "你好", "history": []}
# response = requests.post(url, json = data, stream=True)

# # print response 
# print(response.text) 

# # print iter_content data 
# print(response.iter_content()) 

# # iterates over the list 
# for i in response.iter_content(decode_unicode=True):
#     print(i)


import requests

url = "https://smzx-admin.smzx.inrobot.cloud/rpc/air-ops-srv/Duty.Insert"

for day in range(1, 32):
    print(day)

    payload = {
        "duty_man": "陈希超",
        "phone_number": "17727901230",
        "duty_date": "2023-12-" + str(day),
        "desc": ""
    }
    headers = {
        "authority": "smzx-admin.smzx.inrobot.cloud",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "appkey": "smzx-admin-web",
        "authtoken": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoidXNlciIsInNjb3BlcyI6WyJyb2xlX2I4NmJkMzAzZTlkNTQ5ZTJhNTE2YzNhZGY2NjA2NWUyIl0sIm1ldGFkYXRhIjp7ImNyZWF0ZWQiOiIxNjk1NjMyNjI5IiwiZXhwaXJ5IjoiMTcwMDgxNjYyOSIsInNlY3JldCI6IjIxZTBkZjdkLWE3NjQtNDQ3My1hNWU0LTc2MGM5ZDMwYjA5OCIsInN1YmplY3QiOiJlNThhNzA5Mi01NDcyLTExZWQtODdhNi1iMmU0Njg5ZTdlZjkifSwibmFtZSI6Inpob3VxaTEiLCJleHAiOjE3MDA4MTY2MjksImlhdCI6MTY5NTYzMjYyOSwiaXNzIjoidGVuYW50X2RlZjU2ZTczYjVmNzQxNzc5YjIzN2JmYWJjZGMyOWUwIiwic3ViIjoiZThkMDI1NWUtMWYzOC00YjlkLWE1YmItNmNmNTBjM2FkZWMyIn0.ecl3gfouAuDQ47eK0Y4Y-sGFsBtLvTJJbX0QnOJFIyR4-ilssblvMGz6svQbBrYdTN3eO3_nLD3gXIkW7zfjmqmOIEZUsCz5-s2SbXQN_-qXSsdUP9-eXXitqzJJVOGdqfWJl1mRTFOZK2iJft_NsxAEBWUFoTonC3p-1mCOam4f6toOgcaqMQhEKtjCJFybobNy1opoNemFv_2CSbQb7NnAsr7XZE5hZTwyf9cbR7HP3m7c6mhYKrLGNtAPV_giI_rxL3kz6hV_Q39HnO5T5HW-39PXtNO4cZOPM_n_seXQGpAXnNlJc8c8RQgx3Y1GFsjnGIvjlOG9TK-CdUbS6bkMOvxh7oANj63BSecM2ypOnhX3HuMQ4GelV80EudEmJnNfRqKUcZkQJr61524-rAds3TA_gz4uZEpZac_gTk3yeyB-AWKrpKvnvDDW5zBAV4N3k_ORKzgdl801hDbMD-rbMzt3-Q5UK7qnQpmtSNvdgf2uX0IXwWGEKS8kkkrlQN0hcmIGAvDQctLBBh5-3cWWAyG62vueBzMnePfwDuCQJ1XYI7udCCCK9O0KeUXtYXE0P1gg_vOVhe2Jb67_py-f2gD1QHpbo6xo-SeXwZ3zqCI_t0aNKCYgeKR667U-o_ll2l2EMEGvOTBTL2bEaUDIDOVYFoa7V6GxIaRzcjM",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://smzx-admin.smzx.inrobot.cloud",
        "pragma": "no-cache",
        "referer": "https://smzx-admin.smzx.inrobot.cloud/duty-panel",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
