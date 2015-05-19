import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

threshold_set = [0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]


boc_reuters_21578 = [(0.01,0.338),(0.1,0.336),(0.2,0.316),(0.3,0.283),(0.4,0.262),(0.5,0.260),(0.6,0.211),(0.7,0.172),(0.8,0.108),(0.9,0.018)]

bow_reuters_21578 = [(0.01,0.4092),(0.1,0.4092),(0.2,0.4092),(0.3,0.4092),(0.4,0.4092),(0.5,0.4092),(0.6,0.4092),(0.7,0.4092),(0.8,0.4092),(0.9,0.4092)]

print ''
print ''

print bow_reuters_21578
print boc_reuters_21578

p_bow, = plt.plot(threshold_set,  [x[1] for x in bow_reuters_21578],'r.-')
p_boc, = plt.plot(threshold_set,  [x[1] for x in boc_reuters_21578],'bx-')

plt.legend([p_bow,p_boc], ["BoW F1-score", "BoC F1-score"], loc = "lower right", prop={'size':12})

plt.savefig("Results/img/" + experiment_name)

