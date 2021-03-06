import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/KNN/experiment_knn_20ng_wf_th_0.01_varying_n_neighbors/*.json")
n_neighbors_set = [1, 2, 5, 10, 20, 50, 100, 250]

boc_ohsumed = {}
bow_ohsumed = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoC":
            boc_ohsumed[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW":
            bow_ohsumed[int(json_data['n_neighbors'])] = json_data['f1_score']
           
        print(json_data)

print 
print


boc_ohsumed = sorted(boc_ohsumed.iteritems(), key=operator.itemgetter(0))
bow_ohsumed = sorted(bow_ohsumed.iteritems(), key=operator.itemgetter(0))

print boc_ohsumed
print bow_ohsumed

p_boc, = plt.plot(n_neighbors_set,  [x[1] for x in boc_ohsumed],'b.-')
p_bow, = plt.plot(n_neighbors_set,  [x[1] for x in bow_ohsumed],'rx-')

plt.legend([p_boc, p_bow], ["BoC","BoW"], loc = "lower right")

plt.savefig("Results/img/" + experiment_name)

