"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = False
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = True
# 从环境变量中读取CK（环境变量名：BILIBILI）
# 单账号：直接填CK；多账号：多个CK用英文逗号分隔（需配合main.py的拆分逻辑）

COIN_OR_NOT = True
# 是否投币

COIN_NUM = 5  # 修复：-1改为5，适配NUM_MODE=True的逻辑
# 投币数量：
# - 非NUM_MODE：-1=投满5次（补全当日投币上限）；1-5=指定投币次数
# - NUM_MODE开启：仅投指定次数（1-5），-1无效

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币

STRICT_MODE = False
# 严格模式：保证至少5次成功投币（解决API返回失败但实际投币成功的问题）
# 关闭：仅投5次，无论成功失败（可能少投币，但不会浪费）

NUM_MODE = True
# 与严格模式互斥，开启后仅投COIN_NUM次（无论成功失败）

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']
# 投币UP主的ID号，可替换为自己喜欢的UP主（获取方法见README.md）

COOKIE_LIST = [buvid3=B5A49C16-A35A-57D7-1FD3-B4B901D1776D58303infoc; b_nut=1758763358; _uuid=529106221-2B95-144B-DE78-7FB721026184F58454infoc; enable_web_push=DISABLE; buvid4=11EE6573-254D-24D5-18A7-BED093BEFC2659364-025092509-dxUKD3ypnyS/+P0O/UGPz4nZAIhnD5LGszYRHG+swWAJbwoVUSGilZozjHeSIEmu; buvid_fp=8d65b856981f7f9ed37f396b9fb610dd; SESSDATA=6223752c%2C1774315398%2Cef2d3%2A92CjBwZE0aLBCw-Qauu6uq6YY7rWGcE6xmudS5n3gdmX4La0hfic8ZIt2nEkWZVysk7cASVmQyaDZDUEhJeEYxSzlpeHZKdHM5dkJ4NFpyeDRsZFBzQnc3bC04NV93eGZOb1hVamIyVjJrdklrOXp0NlVYOTYwYVRnQ25TbzFIbjNDR0RPRjNCdGpBIIEC; bili_jct=810ee063a2804f9901b3a71fc6ec63f9; DedeUserID=258872082; DedeUserID__ckMd5=ee5a0e863dc38ae4; theme-tip-show=SHOWED; rpdid=0zbfvRWQXD|WqlFpzQz|410|3w1V1AHW; theme-avatar-tip-show=SHOWED; LIVE_BUVID=AUTO3717588035543497; sid=60cwlynr; theme-switch-show=SHOWED; CURRENT_QUALITY=0; PVID=1; home_feed_column=5; browser_resolution=1698-776; bp_video_offset_258872082=1178477711069282304; theme_style=dark; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQwMTEzNjksImlhdCI6MTc3Mzc1MjEwOSwicGx0IjotMX0.yPPCGssX-EhzeEsBDCe6-SfYn92X8EzYO5u-tvpDYwc; bili_ticket_expires=1774011309; CURRENT_FNVAL=4048; bp_t_offset_258872082=1180775312414212096; b_lsid=9C1126C5_19CFC5431A4]  # 修复：移除冗余的r""，空列表更清晰
# Bilibili的COOKIE（获取方法见README.md），支持多账号：["CK1", "CK2"]

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网：https://www.pushplus.plus

WECHAT_PUSH_OR_NOT = False
# 企业微信推送开关

WECHAT_ID = ""
# 企业ID
WECHAT_SECRET = ""
# 企业应用secret
WECHAT_APP_ID = ""
# 企业应用的id
# 企业应用推送文档：https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# Server酱推送开关（key获取：https://sct.ftqq.com/sendkey）
