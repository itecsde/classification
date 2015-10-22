from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)


feat_labels = df_wine.columns[1:]
forest = RandomForestClassifier(n_estimators=10000,
                               random_state=0,
                                n_jobs=-1)
forest.fit(X_train, y_train)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,  feat_labels[f], importances[indices[f]]))