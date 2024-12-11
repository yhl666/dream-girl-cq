import matplotlib.pyplot as plt

# 设置中文显示，使用微软雅黑字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 如果没有设置字体，则中文可能无法正常显示

plt.rcParams['axes.unicode_minus'] = False
# 解决负号'-'显示为方块的问题
# 定义月份和销量数据
mouth = ['1月', '2月', '3月', '4月', '5月']
# 定义一个 mouth 列表，包含 1-5 月
sales = [27, 90, 20, 111, 23]
# 定义一个 sales 列表，包含 1-5 月的销量数据
liebiao = range(len(mouth))  # 生成月份索引
# 生成一个 mouth_index 列表，包含 0-4 的数字，对应 mouth 列表中的月份
# 创建画布和子图
fig = plt.figure() # 定义个变量fig用来创建一个 Figure 对象，表示整个绘图区域


ax1 = fig.add_subplot(1, 1, 1) # 定义变量 ax1 用来放一个 1x1 的子图，其中包含 1 个子图

ax1.bar(liebiao , sales, align='center', color='darkblue') # 绘制柱状图，柱子宽度为 0.5

# 设置坐标轴位置
ax1.xaxis.set_ticks_position('bottom') # 设置 x 轴刻度标签的位置在底部
ax1.yaxis.set_ticks_position('left') # 设置 y 轴刻度标签的位置在左侧

# 设置刻度标签和旋转角度、字体大小
plt.xticks(liebiao , mouth, rotation=0, fontsize='small')

# 设置坐标轴标签和标题
plt.xlabel('月份')
plt.ylabel('销量')
plt.title('1-5月销量')

# 显示图形
plt.show()
