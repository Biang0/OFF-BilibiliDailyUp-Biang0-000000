"""
Author: Wyatt1026
Project Address: https://github.com/Wyatt1026/BilibiliDailyUp
"""

from core.bilibili import Bilibili
from config import config
import os

if __name__ == '__main__':
    # 初始化CK列表
    ck_list = []
    try:
        if config.USE_ENVIRONMENT_VARIABLE:
            # 读取环境变量 BILIBILI（替换原有的 COOKIES 变量名）
            cookies = os.environ.get('BILIBILI')
            # 检查环境变量是否为空/None
            if not cookies:
                raise ValueError("错误：环境变量 BILIBILI 未配置或值为空！")
            # 拆分多CK（兼容逗号分隔的多账号场景），并过滤空值
            ck_list = [ck.strip() for ck in cookies.split(",") if ck.strip()]
            if not ck_list:
                raise ValueError("错误：环境变量 BILIBILI 的值拆分后无有效CK！")
        else:
            # 从配置文件读取，过滤空值
            ck_list = [ck.strip() for ck in config.COOKIE_LIST if ck.strip()]
            if not ck_list:
                raise ValueError("错误：配置文件 COOKIE_LIST 中无有效CK！")
        
        # 遍历执行每日任务
        for idx, ck in enumerate(ck_list, 1):
            print(f"\n===== 开始处理第 {idx} 个账号 =====")
            bilibili = Bilibili(ck)
            bilibili.go()
            print(f"===== 第 {idx} 个账号处理完成 =====\n")
        
        print("✅ 所有账号任务执行完毕！")

    except ValueError as e:
        # 捕获配置相关的错误，友好提示
        print(f"❌ 配置错误：{e}")
        print("\n请检查：")
        if config.USE_ENVIRONMENT_VARIABLE:
            print("1. 环境变量 BILIBILI 是否已正确配置")
            print("2. 环境变量值是否为有效的B站CK（多账号用英文逗号分隔）")
        else:
            print("1. 配置文件 config.py 中 COOKIE_LIST 是否填写有效CK")
            print("2. COOKIE_LIST 中是否存在空行/无效值")
        exit(1)  # 退出并返回错误码
    except Exception as e:
        # 捕获其他未知错误
        print(f"❌ 程序运行出错：{str(e)}")
        exit(1)
