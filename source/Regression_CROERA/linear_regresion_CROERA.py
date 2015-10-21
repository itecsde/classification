# load numpy and pandas for data manipulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# load statsmodels as alias ``sm``
import statsmodels.api as sm

# load the longley dataset into a pandas data frame - first column (year) used as row labels
df = pd.read_csv('cnx.csv', index_col=0)
df.head()

print df

y = df.F1_cnx  # response
X = df.quality_threshold  # predictor
X = sm.add_constant(X)  # Adds a constant term to the predictor
X.head()

est = sm.OLS(y, X)

est = est.fit()
print est.summary()

print est.params


# Make sure that graphics appear inline in the iPython notebook
#%pylab inline

# We pick 100 hundred points equally spaced from the min to the max
X_prime = np.linspace(X.quality_threshold.min(), X.quality_threshold.max(), 100)[:, np.newaxis]
X_prime = sm.add_constant(X_prime)  # add constant as we did before

# Now we calculate the predicted values
y_hat = est.predict(X_prime)

plt.scatter(X.quality_threshold, y, alpha=0.3)  # Plot the raw data
plt.title("total")
plt.xlabel("quality_threshold")
plt.ylabel("F1")

plt.plot(X_prime[:, 1], y_hat, 'g', alpha=0.9)  # Add the regression line, colored in red
plt.savefig("novale")


