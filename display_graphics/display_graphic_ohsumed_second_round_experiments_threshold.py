import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/ohsumed_BoW_BoC_and_BoC_expanded_with_various_expanded_thresholds/*.json")
threshold_set = [0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

boc_ohsumed = [(0.01,0.4221),(0.1,0.4347),(0.2,0.4248),(0.3,0.4093),(0.4,0.4006),(0.5,0.3921),(0.6,0.3817),(0.7,0.3519),(0.8,0.2909),(0.9,0.0958)]
bow_ohsumed = [(0.01,0.3882),(0.1,0.3882),(0.2,0.3882),(0.3,0.3882),(0.4,0.3882),(0.5,0.3882),(0.6,0.3882),(0.7,0.3882),(0.8,0.3882),(0.9,0.3882)]

print ''
print ''

#bow_ohsumed = sorted(bow_ohsumed.iteritems(), key=operator.itemgetter(1))
#boc_ohsumed = sorted(boc_ohsumed.iteritems(), key=operator.itemgetter(1))

print bow_ohsumed
print boc_ohsumed


p_bow, = plt.plot(threshold_set,  [x[1] for x in bow_ohsumed],'r.-')
p_boc, = plt.plot(threshold_set,  [x[1] for x in boc_ohsumed],'bx-')


plt.legend([p_bow,p_boc], ["BoW F1-score", "BoC F1-score"], loc = "lower right", prop={'size':12})

plt.savefig("Results/img/" + experiment_name)

