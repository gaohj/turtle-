#安装
# pip 是python的包管理工具 也就是 是python 的应用商店 专门用来安装和卸载库用
# pip install itchat
#导入
import itchat

#登录微信

# itchat.login() #每次登录都会让你扫码

def login_info():
    print('微信秘书登录成功')

def logout_info():
    print('微信秘书退出成功')

itchat.auto_login(hotReload=True,loginCallback=login_info,exitCallback=logout_info)
# itchat.login(loginCallback=login_info)
itchat.logout()
# 让机器人一直运行
itchat.run()

