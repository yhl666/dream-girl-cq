# coding=utf-8
# 从sklearn.datasets 导入 iris数据加载器。
from sklearn.datasets import load_iris
# 使用加载器读取数据并且存入变量iris。
iris = load_iris()
# 从sklearn.cross_validation里选择
# 导入train_test_split用于数据分割。
from sklearn.model_selection import train_test_split
# 从使用train_test_split，利用随机种子
# random_state采样25%的数据作为测试集。
X_train, X_test, y_train, y_test = train_test_split(\
   iris.data, iris.target, test_size=0.25, random_state=33)
# 从sklearn.preprocessing里选择导入数据标准化模块。
from sklearn.preprocessing import StandardScaler
# 从sklearn.neighbors里选择导入KNeighborsClassifier，\
# 即K近邻分类器。
from sklearn.neighbors import KNeighborsClassifier

# 对训练和测试的特征数据进行标准化。
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# 使用K近邻分类器对测试数据进行类别预测，预测结果储存在变量y_predict中。
knc = KNeighborsClassifier()
knc.fit(X_train, y_train)
y_predict = knc.predict(X_test)
print 'The accuracy of K-Nearest Neighbor Classifier is',\
   knc.score(X_test, y_test)
from sklearn.metrics import classification_report
print classification_report(y_test, y_predict, \
                            target_names=iris.target_names)