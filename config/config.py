"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = True
# 投币时是否点赞

# ====================== 改这里 1 ======================
USE_ENVIRONMENT_VARIABLE = False  # 必须关闭！这个功能是坏的！
# ======================================================

COIN_OR_NOT = True
# 是否投币

COIN_NUM = -1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币

STRICT_MODE = True
# 是否开启严格模式
NUM_MODE = False

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']

# ====================== 改这里 2 ======================
# 把你自己的 Cookie 原样填回去！
COOKIE_LIST = [
    r"buvid3=B5A49C16-A35A-57D7-1FD3-B4B901D1776D58303infoc; b_nut=1758763358; _uuid=529106221-2B95-144B-DE78-7FB721026184F58454infoc; enable_web_push=DISABLE; buvid4=11EE6573-254D-24D5-18A7-BED093BEFC2659364-025092509-dxUKD3ypnyS/+P0O/UGPz4nZAIhnD5LGszYRHG+swWAJbwoVUSGilZozjHeSIEmu; buvid_fp=8d65b856981f7f9ed37f396b9fb610dd; SESSDATA=6223752c%2C1774315398%2Cef2d3%2A92CjBwZE0aLBCw-Qauu6uq6YY7rWGcE6xmudS5n3gdmX4La0hfic8ZIt2nEkWZVysk7cASVmQyaDZDUEhJeEYxSzlpeHZKdHM5dkJ4NFpyeDRsZFBzQnc3bC04NV93eGZOb1hVamIyVjJrdklrOXp0NlVYOTYwYVRnQ25TbzFIbjNDR0RPRjNCdGpBIIEC; bili_jct=810ee063a2804f9901b3a71fc6ec63f9; DedeUserID=258872082; DedeUserID__ckMd5=ee5a0e863dc38ae4; theme-tip-show=SHOWED; rpdid=0zbfvRWQXD|WqlFpzQz|410|3w1V1AHW; theme-avatar-tip-show=SHOWED; LIVE_BUVID=AUTO3717588035543497; sid=60cwlynr; theme-switch-show=SHOWED; CURRENT_QUALITY=0; PVID=1; home_feed_column=5; browser_resolution=1698-776; bp_video_offset_258872082=1178477711069282304; theme_style=dark; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQwMTEzNjksImlhdCI6MTc3Mzc1MjEwOSwicGx0IjotMX0.yPPCGssX-EhzeEsBDCe6-SfYn92X8EzYO5u-tvpDYwc; bili_ticket_expires=1774011309; CURRENT_FNVAL=4048; bp_t_offset_258872082=1180775312414212096; b_lsid=9C1126C5_19CFC5431A4"
]
# ======================================================

PUSH_OR_NOT = False
TOKEN = ''

WECHAT_PUST_OR_NOT = True
WECHAT_ID = ""
WECHAT_SECRET = ""
WECHAT_APP_ID = ""

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
