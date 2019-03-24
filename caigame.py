#Author:黄国栋
age=23
num=0
while num<3:
    age1=int(input("请输入年龄:"))
    if age==age1:
        print("猜对了")
        break
    elif age<age1:
        print("猜大了")
    else:
        print("猜小了")
    num+=1
    if num==3:
        print("您已经超过三次机会。。。不好意思，小爷不陪你玩了")


