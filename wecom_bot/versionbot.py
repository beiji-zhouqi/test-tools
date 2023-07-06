# 一个演示程序
from corpwechatbot.chatbot import CorpWechatBot

bot = CorpWechatBot(key='')  # 你的机器人key，通过群聊添加机器人获取
bot.send_text(content="test", # 你想要发的文本内容
              mentioned_list=[], # 用户userid
              mentioned_mobile_list=['', '', '', '', '', ''])  # 用户手机号码