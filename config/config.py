"""
The config for this script, you can read the description in README.md
"""
import os

LIKE_OR_NOT = False
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = True
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = -1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = False
# 是否将银瓜子兑换为硬币

STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择
NUM_MODE = False
# 该模式与严格模式互斥,开启此模式,投币只会投COIN_NUM次,无论成功失败

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118', '456664753']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md

COOKIE_LIST = [
    r"buvid3=AD30B5E5-C60A-93EF-4061-4380AA2F43EB66150infoc; b_nut=1740625166; _uuid=B211044F10-4FA8-3986-D10E6-D46D5F53133C98500infoc; fingerprint=3f78ebdcc7a3398b43234dc5a91ff8ea; buvid_fp_plain=undefined; buvid4=D70363DF-5C51-CBE5-FB82-C0803F99573C96834-025022702-gTcIbaPYCZFL0BBWj2earQ%3D%3D; buvid_fp=3f78ebdcc7a3398b43234dc5a91ff8ea; header_theme_version=CLOSE; enable_web_push=DISABLE; DedeUserID=258872082; DedeUserID__ckMd5=ee5a0e863dc38ae4; rpdid=|(J~JJRYYmRR0J'u~R|Yklk~|; hit-dyn-v2=1; enable_feed_channel=ENABLE; PVID=1; bp_video_offset_258872082=1044937282231992320; CURRENT_FNVAL=4048; bp_t_offset_258872082=1045221248289734656; home_feed_column=5; browser_resolution=1528-751; SESSDATA=374e6708%2C1758013870%2C58c9b%2A32CjCFZuGQew7xVVnygutL5p-gwwtfBbJO_tvPQFVqOerEIrqbLCqwqTvjk9Os85TJo2ISVnFZY21yR2NzLU9aTTF4aHFVRV9iRjlSeXhrMV82bUdLVkZ3bHhDUWdTWVZUaVJOTllTOWNTSTJWa0JYdE9ZVjhUYlRoS0dYR2p4M0hldzlrTVVyeGt3IIEC; bili_jct=c40793f6e49da8544cae4388c59ba989; sid=4h48sic6; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI4Njg5MjQsImlhdCI6MTc0MjYwOTY2NCwicGx0IjotMX0.uyV2j6KwRqDfyx4O2EdwcpUpgxtwaaOqi84P39tLTZk; bili_ticket_expires=1742868864",  
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

WECHAT_PUSH_OR_NOT = False
# 默认关闭企业微信推送

WECHAT_ID = os.environ.get('WECHAT_ID')
# 企业ID
WECHAT_SECRET = os.environ.get('WECHAT_SECRET')
# 企业应用secret
WECHAT_APP_ID = os.environ.get('WECHAT_APP_ID')
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = True
SERVER_KEY = os.environ.get('SERVER_KEY')
if SERVER_KEY is None:
    print("警告: SERVER_KEY 未设置，请检查环境变量。")
else:
    print(f"获取到的 SERVER_KEY: {SERVER_KEY}")
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key
