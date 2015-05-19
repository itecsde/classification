import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

threshold_set = [0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

boc_ohsumed = [(0.01,0.71645),(0.1,0.5753),(0.2,0.5333),(0.3,0.5001),(0.4,0.4743),(0.5,0.4361),(0.6,0.401),(0.7,0.3368),(0.8,0.214),(0.9,0.0059)]
bow_ohsumed = [(0.01,0.7429),(0.1,0.7429),(0.2,0.7429),(0.3,0.7429),(0.4,0.7429),(0.5,0.7429),(0.6,0.7429),(0.7,0.7429),(0.8,0.7429),(0.9,0.7429)]

print ''
print ''

print bow_ohsumed
print boc_ohsumed

p_bow, = plt.plot(threshold_set,  [x[1] for x in bow_ohsumed],'r.-')
p_boc, = plt.plot(threshold_set,  [x[1] for x in boc_ohsumed],'bx-')


plt.legend([p_bow,p_boc], ["BoW F1-score", "BoC F1-score"], loc = "lower right", prop={'size':12})

plt.savefig("Results/img/" + experiment_name)

