from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

'''
X = np.arange(6).reshape(3, 2)

print X

poly = PolynomialFeatures(degree=2)
poly.fit_transform(X)

print poly.fit_transform(X)


model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                   ('linear', LinearRegression(fit_intercept=False))])


x = np.arange(5)
y = 3 - 2 * x + x ** 2 - x ** 3
model = model.fit(x[:, np.newaxis], y)
model.named_steps['linear'].coef_

print model.named_steps['linear'].coef_

'''

results = {}

y_oercommons = np.array([0.27,0.27,0.27,0.273,0.273,0.273,0.273,0.277,0.274,0.276,0.275,0.285,0.278,0.278,0.316,0.365,0.398])

y_cnx = np.array([0.582,0.582,0.582,0.585,0.585,0.585,0.585,0.591,0.592,0.598,0.642,0.646,0.658,0.654,0.667,0.693,0.698])

y_merlot = np.array([0.522,0.522,0.522,0.524,0.524,0.524,0.524,0.53,0.528,0.542,0.554,0.559,0.564,0.595,0.599,0.615,0.573])

y = y_cnx

y = np.concatenate((y_oercommons, y_cnx, y_merlot))

y_media = (y_oercommons + y_cnx + y_merlot) / 3.0

y = y_media

y = y_cnx


x = np.array([0,0.05,0.1,0.15,0.20,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8])

#x = np.concatenate((x, x,x))

print x


z = np.polyfit(x, y, 2)

results['polynomial'] = z.tolist()

p = np.poly1d(z)

yhat = p(x)                         # or [p(z) for z in x]
ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
results['determination'] = ssreg / sstot

print results

p30 = np.poly1d(np.polyfit(x, y, 30))

xp = np.linspace(0, 0.8, 100)

_ = plt.plot(x, y, '.', xp, p(xp), '-')

plt.ylim(0.57,0.72)

plt.title("total")
plt.xlabel("quality_threshold")
plt.ylabel("F1")


plt.show()

#plt.savefig("borrar")