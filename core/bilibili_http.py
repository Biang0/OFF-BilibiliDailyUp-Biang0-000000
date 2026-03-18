# core/bilibili_http.py 2026最新修复版
import requests
import time

class BilibiliHttp:
    def __init__(self, cookie: str):
        self.cookie = cookie.strip()
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Cookie": self.cookie,
            "Referer": "https://www.bilibili.com/"
        }
        self.csrf = self.get_csrf()

    def get_csrf(self):
        for i in self.cookie.split("; "):
            if i.startswith("bili_jct="):
                return i.split("=")[1]
        return ""

    # 1. Cookie有效性校验
    def get_cookie_status(self):
        try:
            res = self.session.get("https://api.bilibili.com/x/web-interface/nav", timeout=10)
            return res.json().get("data", {}).get("isLogin", False)
        except:
            return False

    # 2. 获取个人信息
    def get_info(self):
        try:
            res = self.session.get("https://api.bilibili.com/x/web-interface/nav", timeout=10)
            data = res.json()["data"]
            return f"用户名：{data['uname']} | 硬币：{data['coins']} | 等级：{data['level_info']['current_level']}"
        except:
            return "获取信息失败"

    # 3. 直播签到
    def live_sign(self):
        try:
            res = self.session.get("https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/WebSign", timeout=10)
            j = res.json()
            if j["code"] == 0:
                return "✅ 直播签到成功"
            elif "重复" in str(j):
                return "✅ 直播已签到"
            else:
                return "❌ 直播签到失败"
        except:
            return "❌ 直播签到接口异常"

    # 4. 查询直播银瓜子
    def inquire_live_info(self):
        try:
            res = self.session.get("https://api.live.bilibili.com/xlive/web-interface/v1/liveWallet/getWallet", timeout=10)
            return int(res.json()["data"]["silver"])
        except:
            return 0

    # 5. 银瓜子兑换硬币
    def silver_to_coin(self):
        try:
            res = self.session.post("https://api.live.bilibili.com/xlive/revenue/v1/order/silver2coin", data={
                "csrf": self.csrf
            })
            j = res.json()
            if j["code"] == 0:
                return {"status": True, "msg": self.inquire_live_info()}
            return {"status": False, "msg": j.get("message", "兑换失败")}
        except:
            return {"status": False, "msg": "接口异常"}

    # 6. 漫画签到
    def check_comics_sign(self):
        try:
            res = self.session.get("https://manga.bilibili.com/twapiservice/v1/user/sign/info", timeout=10)
            return res.json()["data"]["is_sign"]
        except:
            return False

    def comics_sign(self):
        try:
            self.session.post("https://manga.bilibili.com/twapiservice/v1/user/sign")
            return True
        except:
            return False

    # 7. 获取视频列表
    def get_video_list(self):
        try:
            res = self.session.get("https://api.bilibili.com/x/web-interface/index/top/rcmd", timeout=10)
            data = res.json()["data"]["item"]
            return [(i["bvid"], i["title"], i["owner"]["name"], i["aid"]) for i in data[:10]]
        except:
            return []

    # 8. 投币
    def insert_coin(self, aid):
        try:
            data = {
                "aid": aid,
                "multiply": 1,
                "csrf": self.csrf,
                "like": 0
            }
            res = self.session.post("https://api.bilibili.com/x/web-interface/coin/add", data=data)
            return res.json()["code"] == 0
        except:
            return False

    # 9. 观看视频
    def watch_video(self, bvid):
        try:
            self.session.get(f"https://api.bilibili.com/x/click-interface/web/heartbeat?bvid={bvid}&played_time=30")
            time.sleep(1)
        except:
            pass

    # 10. 分享视频
    def share_video(self, bvid):
        try:
            self.session.post("https://api.bilibili.com/x/web-interface/share/add", data={
                "bvid": bvid,
                "csrf": self.csrf
            })
        except:
            pass

    # 11. 查询每日任务状态
    def inquire_job(self):
        try:
            res = self.session.get("https://api.bilibili.com/x/member/web/exp/reward", timeout=10)
            data = res.json()["data"]
            return {
                "login": True,
                "watch": data["watch"],
                "share": data["share"],
                "insert": data["coin"]
            }
        except:
            return {"login":True,"watch":False,"share":False,"insert":0}
