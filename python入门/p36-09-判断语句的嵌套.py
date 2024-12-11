"""
if int(input("你的身高多少："))>120:
    print("身高超出限制,不可以免费")
    print("但是,如果vip等级大于3,可以免费")

    if int(input("vip等级是多少:"))>3:
        print("恭喜你,vip等级达标,可以免费")
    else:
        print("很遗憾,你需要购票10元")
else:
    print("欢迎小朋友,可以免费")
"""
"""
age=310  # 年龄
year=3  # 入职时间
lv=1    # 工作级别
if age>=18:
    print("你是成年人")
    if age <30:
        print("你的年龄达标了")
        if year >2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif lv>3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("很遗憾，年龄达标，但是入职时间和级别不达标")
    else:
        print("你的年龄太大了")
else:
    print("不好意思小朋友不可以领取")
"""
age=int(input("请输入你的年龄:"))  # 年龄
year=int(input("请输入职时间:"))  # 入职时间
lv=int(input("请输入工作级别:"))    # 工作级别
if age>=18:
    print("你是成年人")
    if age <30:
        print("你的年龄达标了")
        if year >2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif lv>3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("很遗憾，年龄达标，但是入职时间和级别不达标")
    else:
        print("你的年龄太大了")
else:
    print("不好意思小朋友不可以领取")