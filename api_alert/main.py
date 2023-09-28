from corpwechatbot.chatbot import CorpWechatBot
import requests
import json
import time
import os


Bot_key = "f29963d2-2084-42d4-949f-9713484ea047"
directory_path = "./data"
run_result = []


# 发送到weChat
def weChatBot(case_total, num, rate_case_success):
    bot = CorpWechatBot(Bot_key)  # 你的机器人key，通过群聊添加机器人获取
    bot.send_text(content=("**********接口测试报告**********\n" +
                           "接口用例数量:" + case_total + "\n" +
                           "用例失败数量:" + num + "\n" +
                           "用例执行成功率:" + rate_case_success + "%" + "\n"), # 你想要发的文本内容
                  mentioned_list=[], # 用户userid
                  mentioned_mobile_list=['', '', '', '', '', ''])  # 用户手机号码
    

# 读取指定目录下所有脚本
def get_all_files_in_directory():
    # 存储所有文件的列表
    file_list = []

    # 使用os.walk遍历目录及其子目录中的文件
    for root, _, files in os.walk(directory_path):
        for file in files:
            # 获取文件的完整路径并添加到文件列表中
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    return file_list


# 读取接口
def get_apicase_in_file():

    for file in get_all_files_in_directory():
        with open(file=file, mode='r', encoding='utf-8') as f:
            result = json.load(f)
    return result


if __name__ == "__main__":
    # 登录
    login_url = 'https://air-sso.uat.inrobot.cloud/rpc/platform-iam/IAM.Login'
    login_body = "{\"username\":\"zhouqi1\",\"password\":\"aGVsbG95aW5naGUxMjMjLg==\",\"device\":\"web\",\"login_method\":\"LOGIN_METHOD_LDAP\"}"
    req = requests.post(login_url, json=login_body)
    token = req.json()['token']
    
    # 读取脚本
    result = get_apicase_in_file()
    for key, value in result.items():
        for sub_key, sub_value in value.items():
            assert_data = ''
            url = sub_value['url']
            method = sub_value['method']
            headers = {header['name']: header['value'] for header in sub_value['headers']}
            for key in sub_value.keys():
                if 'assert' in key:
                    assert_data = sub_value['assert']
                    print(assert_data)
            
            for header in headers:
                if header == "AuthToken":
                    headers[header] = "Bearer " + token
    # 处理脚本
    # 执行脚本
            if method == "GET":
                response = requests.get(url, headers=headers)
                if response.status_code == 200 and assert_data in response.text:
                    assert_result = 'SUCCESS'
                else:
                    assert_result = 'FAIL'
            elif method == "POST":
                body = sub_value["body"][0]  # POST请求的body为列表中的第一个元素
                response = requests.post(url, json=body, headers=headers)
                if response.status_code == 200 and assert_data in response.text:
                    assert_result = 'SUCCESS'
                else:
                    assert_result = 'FAIL'
            run_result.append({"测试用例名称": sub_key, "请求URL": url, "请求方法": method, "响应状态码": response.status_code,  "断言结果": assert_result})
                
    # 存储执行数据
    case_total = len(run_result)
    num = 0
    for case in run_result:
        if case['断言结果'] == 'FAIL':
            num +=1
    num_case_fail = num
    rate_case_success = (case_total - num) / case_total * 100
    print(run_result)
    print(f"接口用例数量: {case_total}")
    
    print(f"用例失败数量：{num}")
    print(f"用例执行成功率：{rate_case_success}%")
    # 生成报告
    # 发送数据到weChat
    weChatBot(str(case_total), str(num), str(rate_case_success))
