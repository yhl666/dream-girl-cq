#ch4-25_DisplayBargraph
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #����������ʾ���ı�ǩ
plt.rcParams['axes.unicode_minus']=False #����������ʾ����
month = ['һ��', '����', '����', '����', '����']
sale_amounts = [27, 90, 20, 111, 23]
month_index = range(len(month))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(month_index, sale_amounts, align='center', color='darkblue')
plt.xticks(month_index, month, rotation=0, fontsize='small')
plt.xlabel('�·�')
plt.ylabel('���۶�')
plt.title('ÿ���µ����۶�')
plt.show()