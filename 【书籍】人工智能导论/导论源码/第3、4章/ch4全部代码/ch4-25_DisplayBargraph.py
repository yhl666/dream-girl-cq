#ch4-25_DisplayBargraph
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
month = ['一月', '二月', '三月', '四月', '五月']
sale_amounts = [27, 90, 20, 111, 23]
month_index = range(len(month))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(month_index, sale_amounts, align='center', color='darkblue')
plt.xticks(month_index, month, rotation=0, fontsize='small')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.title('每个月的销售额')
plt.show()