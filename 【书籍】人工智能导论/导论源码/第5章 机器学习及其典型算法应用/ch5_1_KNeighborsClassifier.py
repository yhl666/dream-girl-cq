# coding=utf-8
# print 'this is a string' #python2.7
# print('this is a string') #python3
from sklearn.neighbors import KNeighborsClassifier
X = [[0], [1], [2], [3],[4], [5], [6], [7], [8]]#9个１维的数据
y = [0, 0, 0, 1, 1, 1, 2, 2, 2]#9个数据对应的类标号
neigh = KNeighborsClassifier(n_neighbors=3)#3近邻
neigh.fit(X, y)#X为训练数据，y为目标值训练模型
print(neigh.predict([[1.1]]))#预测提供数据的类别
print neigh.predict([[1.6]])
print neigh.predict([[5.2]])
print neigh.predict([[5.8]])
print neigh.predict([[6.2]])
