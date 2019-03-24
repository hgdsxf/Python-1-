#Author:黄国栋
username1="abc"
password1="123456"
username=input("姓名：")
password=input("密码：")

if username==username1 and password==password1:
    print("欢迎用户{username2}登录成功。。。".format(username2=username1))
else:
    print("登录失败")