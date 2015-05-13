import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/*.json")
train_set = [5, 10, 50]


bow_ieee = {}
boc_ieee = {}
boc_ieee_expanded = {}

sys.stdout = open("Results/outputs/" + experiment_name + ".txt", 'w')

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow_ieee[int(json_data['train'])] = json_data['f1_score']
        elif json_data['expansion_threshold'] == None:
            boc_ieee[int(json_data['train'])] = json_data['f1_score']
        elif json_data['expansion_threshold'] != None:
            boc_ieee_expanded[int(json_data['train'])] = json_data['f1_score']
            
        print(json_data)

print 
print

bow_ieee = sorted(bow_ieee.iteritems(), key=operator.itemgetter(1))
boc_ieee = sorted(boc_ieee.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded = sorted(boc_ieee_expanded.iteritems(), key=operator.itemgetter(1))

print bow_ieee
print boc_ieee
print boc_ieee_expanded

p_bow, = plt.plot(train_set,  [x[1] for x in bow_ieee],'g*-')
p_boc, = plt.plot(train_set,  [x[1] for x in boc_ieee],'b.-')
p_boc_exp, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded],'rx-')
plt.legend([p_bow,p_boc,p_boc_exp], ["BoW", "BoC","BoC expanded"], loc = "lower right")
#plt.show()
plt.savefig("Results/img/" + experiment_name)

