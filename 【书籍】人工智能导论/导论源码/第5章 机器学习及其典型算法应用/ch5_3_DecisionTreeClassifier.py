# coding=utf-8
from itertools import product
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
iris = datasets.load_iris()  #仍然使用自带的iris数据
X = iris.data[:, [0, 2]]
y = iris.target
clf = DecisionTreeClassifier(max_depth=4)  # 训练模型，限制树的最大深度4
clf.fit(X, y)  # 拟合模型
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1  # 画图
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),np.arange(y_min, y_max, 0.1))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
plt.show()



