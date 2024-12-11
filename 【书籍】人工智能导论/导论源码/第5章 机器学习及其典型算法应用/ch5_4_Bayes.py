from sklearn import datasets
iris = datasets.load_iris()
from sklearn import naive_bayes
gnb = naive_bayes.GaussianNB()
gnb.fit(iris.data, iris.target)
y_pred = gnb.predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d"\
      % (iris.data.shape[0],(iris.target != y_pred).sum()))