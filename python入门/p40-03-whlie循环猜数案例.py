import random
num=random.randint(1,100)   # 随机1-100之间的数
print(num)

# 通过一个布尔变量，循环是否继续标记
flag=True
count=0 #定义一个变量计算总共猜了多少次
while flag:   #猜错了，每次进入while循环，继续猜
    bj_num=int(input("请输入你想猜的数："))
    count+=1  #累计计算猜了多少次
    if bj_num==num:
        print("恭喜你猜对了！")

        #设置false就是循环终止的条件
        flag=False

    else:
        if bj_num>num:
            print("你猜的数大了")
        else:
            print("你猜的数小了")
print(f"你总共猜了{count}次")