import json

# 读取JSON文件内容
with open("data.json") as f:
    data = json.load(f)

# 根据数据执行操作
if data["operation"] == "add":
    result = sum(data["operands"])
elif data["operation"] == "multiply":
    result = 1
    for operand in data["operands"]:
        result *= operand
else:
    result = "Unknown operation"

print("Result:", result)
