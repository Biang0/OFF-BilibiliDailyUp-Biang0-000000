"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = False
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = True
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = -1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币

STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择
NUM_MODE = True
# 该模式与严格模式互斥,开启此模式,投币只会投COIN_NUM次,无论成功失败

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md

COOKIE_LIST = [
    r"buvid3=B5A49C16-A35A-57D7-1FD3-B4B901D1776D58303infoc; b_nut=1758763358; _uuid=529106221-2B95-144B-DE78-7FB721026184F58454infoc; enable_web_push=DISABLE; buvid4=11EE6573-254D-24D5-18A7-BED093BEFC2659364-025092509-dxUKD3ypnyS/+P0O/UGPz4nZAIhnD5LGszYRHG+swWAJbwoVUSGilZozjHeSIEmu; buvid_fp=8d65b856981f7f9ed37f396b9fb610dd; SESSDATA=6223752c%2C1774315398%2Cef2d3%2A92CjBwZE0aLBCw-Qauu6uq6YY7rWGcE6xmudS5n3gdmX4La0hfic8ZIt2nEkWZVysk7cASVmQyaDZDUEhJeEYxSzlpeHZKdHM5dkJ4NFpyeDRsZFBzQnc3bC04NV93eGZOb1hVamIyVjJrdklrOXp0NlVYOTYwYVRnQ25TbzFIbjNDR0RPRjNCdGpBIIEC; bili_jct=810ee063a2804f9901b3a71fc6ec63f9; DedeUserID=258872082; DedeUserID__ckMd5=ee5a0e863dc38ae4; theme-tip-show=SHOWED; rpdid=0zbfvRWQXD|WqlFpzQz|410|3w1V1AHW; theme-avatar-tip-show=SHOWED; LIVE_BUVID=AUTO3717588035543497; sid=60cwlynr; theme-switch-show=SHOWED; CURRENT_QUALITY=0; PVID=1; home_feed_column=5; browser_resolution=1698-776; bp_video_offset_258872082=1178477711069282304; theme_style=dark; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQwMTEzNjksImlhdCI6MTc3Mzc1MjEwOSwicGx0IjotMX0.yPPCGssX-EhzeEsBDCe6-SfYn92X8EzYO5u-tvpDYwc; bili_ticket_expires=1774011309; CURRENT_FNVAL=4048; bp_t_offset_258872082=1180775312414212096; b_lsid=9C1126C5_19CFC5431A4"
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

# ==============================================
# 这里修复了：PUST → PUSH
WECHAT_PUSH_OR_NOT = False
# ==============================================

WECHAT_ID = ""
# 企业ID
WECHAT_SECRET = ""
# 企业应用secret
WECHAT_APP_ID = ""
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key
