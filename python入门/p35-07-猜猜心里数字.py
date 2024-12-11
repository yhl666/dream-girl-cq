num=5


if int(input("请输入你想猜的数字："))==num:
    print("恭喜你，第一次就猜对了")
elif int(input("猜错了,再猜一次:"))==num:
    print("恭喜你，答对了")
elif int(input("猜错了,最后再猜一次:"))==num:
    print("恭喜你，最后一次猜对了")
else:
    print("很遗憾，你没有猜对")