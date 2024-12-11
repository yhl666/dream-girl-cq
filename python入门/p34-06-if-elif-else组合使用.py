sg = int(input("请输入你的身高"))
vip=int(input("请输入你的VIP等级"))
day=int(input("请输入游玩日期"))

if sg<120:
    print("你的身高没有超过120cm，可以免费游玩")
elif vip>=3:
    print("你的VIP等级超过3，可以免费游玩")
elif day==1:
    print("今天是1号，可以免费游玩")
else:
    print("不好意思条件都不满足，需要购票10元")
print("\n")


# 简写方式
if int(input("请输入你的身高"))<120:
    print("你的身高没有超过120cm，可以免费游玩")
elif int(input("请输入你的VIP等级"))>=3:
    print("你的VIP等级超过3，可以免费游玩")
elif int(input("请输入游玩日期")):
    print("今天是1号，可以免费游玩")
else:
    print("不好意思条件都不满足，需要购票10元")