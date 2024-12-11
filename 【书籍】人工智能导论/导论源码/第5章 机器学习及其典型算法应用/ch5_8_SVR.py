import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - np.random.rand(8))
svr_rbf1 = SVR(kernel='rbf', C=100, gamma=0.1)
y_rbf1 = svr_rbf1.fit(X, y).predict(X)
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X, y_rbf1, linestyle='-', lw=lw, label='RBF gamma=1.0')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()