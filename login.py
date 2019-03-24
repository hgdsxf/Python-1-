#Author:黄国栋
username="abc"
password="123456"

num=0
while num <3:
    username1=input("请输入姓名:")
    password1=input("请输入密码:")
    if username1==username and password1==password:
        print("用户名{username2}登录系统成功。。。".format(username2=username1))
        break
    else:
        print("用户名或密码输入错误，请您重新输入")
    num+=1
    if num==3:
        print("不好意思，您的账号或密码已经错了三次,小爷不玩了")