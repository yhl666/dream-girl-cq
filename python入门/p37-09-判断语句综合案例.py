import random  
#导入随机数库
num=random.randint(1,10)
#   print("随机数是:",num)
cc=int(input("请输入你猜的数字："))
if cc==num:
    print("恭喜你，第一次就猜对了")
else:
    if cc>num:
        print("你猜的数字偏大")
    else:
        print("你猜的数字偏小")
    cc=int(input("请输入你猜的数字："))  #在输入，重新猜测


    if cc==num:
        print("恭喜你，第二次就猜对了")
    else:
        if cc>num:
            print("你猜的数字偏大")
        else:
            print("你猜的数字偏小")
            cc=int(input("请输入你猜的数字："))  #在输入，重新猜测

    if cc==num:
        print("恭喜你，第三次就猜对了")
    else:
        print("很遗憾，你没有猜对")




