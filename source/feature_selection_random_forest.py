from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
print X.shape
clf = ExtraTreesClassifier()
X_new = clf.fit(X, y).transform(X)
print clf.feature_importances_
print X_new.shape