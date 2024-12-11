import matplotlib.pyplot as plt

# 绘制一条直线
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)

# 添加标题
plt.title("简单折线图")

# 添加 x 轴和 y 轴标签
plt.xlabel("x")
plt.ylabel("y")

# 显示图形
plt.show()
