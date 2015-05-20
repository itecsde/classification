import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_folder = sys.argv[1]

json_files =  glob.glob("Results/json/KNN/" + experiment_folder +"/*.json")
n_neighbors_set = [1, 2, 5, 10, 20, 50, 100, 250]
ohsumed_n_neighbors_set = [1, 2, 5, 10, 15, 20, 50, 100, 250]

boc = {}
bow = {}
boc_expanded = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
	corpus = json_data['corpus']
	if 'expanded' in json_data['corpus']:
            boc_expanded[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoC":
            boc[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW":
            bow[int(json_data['n_neighbors'])] = json_data['f1_score']
           
        print(json_data)

print 
print


boc = sorted(boc.iteritems(), key=operator.itemgetter(0))
bow = sorted(bow.iteritems(), key=operator.itemgetter(0))
boc_expanded = sorted(boc_expanded.iteritems(), key=operator.itemgetter(0))

print boc
print bow
print boc_expanded

if "ohsumed" in corpus:
	p_boc, = plt.plot(ohsumed_n_neighbors_set,  [x[1] for x in boc],'b.-')
	p_bow, = plt.plot(ohsumed_n_neighbors_set,  [x[1] for x in bow],'rx-')
	p_boc_expanded, = plt.plot(ohsumed_n_neighbors_set,  [x[1] for x in boc_expanded],'g*-')
else:
	p_boc, = plt.plot(n_neighbors_set,  [x[1] for x in boc],'b.-')
	p_bow, = plt.plot(n_neighbors_set,  [x[1] for x in bow],'rx-')
	p_boc_expanded, = plt.plot(n_neighbors_set,  [x[1] for x in boc_expanded],'g*-')

plt.title(experiment_folder)
plt.xlabel('n_neighbors')
plt.ylabel('F1-score')
plt.legend([p_boc, p_bow, p_boc_expanded], ["BoC","BoW","BoC_expanded"], loc = "lower right")

plt.savefig("Results/json/KNN/" + experiment_folder + "/" + experiment_folder.replace(".","_"))

