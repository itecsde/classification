

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
# import formula api as alias smf
import statsmodels.formula.api as smf

# formula: response ~ predictor + predictor
#est = smf.ols(formula='Sales ~ TV + Radio', data=df_adv).fit()
import sys

df_adv = pd.read_csv('cnx.csv', index_col=0)

y = df_adv.F1_cnx  # response
X = df_adv.quality_threshold  # predictor
X = sm.add_constant(X)  # Adds a constant term to the predictor
X.head()

## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

print "LINEAR"

print est.summary()

print "---------------------------------------------------------------"

df = pd.read_csv('cnx.csv')

# plot lstat (% lower status of the population) against median value
plt.figure(figsize=(6 * 1.618, 6))
plt.scatter(df.quality_threshold, df.F1_mean, s=10, alpha=0.3)
plt.ylabel('F1')
plt.xlabel('quality_threshold')

# points linearlyd space on lstats
x = pd.DataFrame({'quality_threshold': np.linspace(df.quality_threshold.min(), df.quality_threshold.max(), 100)})


# 2-nd order polynomial
poly_2 = smf.ols(formula='F1_mean ~ 1 + quality_threshold + I(quality_threshold ** 2.0)', data=df).fit()


if poly_2.params[1] < 0 and poly_2.params[0] < 0:

    plt.plot(x.quality_threshold, poly_2.predict(x), 'g-',
             label='$R^2$ = {:1.3f} \n $p-value$ = {:1.8f} \n NOBS = {} \n $y$={:1.3f}$x^2$ -{:1.3f}$x$ -{:1.3f}'.format(poly_2.rsquared,poly_2.f_pvalue,int( poly_2.nobs),poly_2.params[2],abs(poly_2.params[1]),abs(poly_2.params[0])),
             alpha=0.9)

elif poly_2.params[1] < 0 and poly_2.params[0] > 0:

    plt.plot(x.quality_threshold, poly_2.predict(x), 'g-',
             label='$y$={:1.3f}$x^2$ -{:1.3f}$x$ +{:1.3f} \n $p-value$ = {:1.12f} \n $R^2$ = {:1.3f} \n NOBS = {}'.format(poly_2.params[2],abs(poly_2.params[1]),abs(poly_2.params[0]), poly_2.f_pvalue, poly_2.rsquared, int(poly_2.nobs)),
             alpha=0.9)

elif poly_2.params[1] > 0 and poly_2.params[0] < 0:

    plt.plot(x.quality_threshold, poly_2.predict(x), 'g-',
             label='$R^2$ = {:1.3f} \n $p-value$ = {:1.12f} \n NOBS = {} \n $y$={:1.3f}$x^2$ +{:1.3f}$x$ -{:1.3f}'.format(poly_2.rsquared,poly_2.f_pvalue, int(poly_2.nobs),poly_2.params[2],abs(poly_2.params[1]),abs(poly_2.params[0])),
             alpha=0.9)

elif poly_2.params[1] > 0 and poly_2.params[0] > 0:

    plt.plot(x.quality_threshold, poly_2.predict(x), 'g-',
             label='$R^2$ = {:1.3f} \n $p-value$ = {:1.8f} \n NOBS = {} \n $y$={:1.3f}$x^2$ +{:1.3f}$x$ +{:1.3f}'.format(poly_2.rsquared,poly_2.f_pvalue, int(poly_2.nobs),poly_2.params[2],abs(poly_2.params[1]),abs(poly_2.params[0])),
             alpha=0.9)


print "POLY_2_SUMMARY"

print poly_2.summary()

figure_title = sys.argv[1]

plt.title("Average")

plt.legend(loc = "upper left", prop={'size':12})

plt.ylim([0.45,0.57])

#plt.show()

plt.savefig(figure_title)
