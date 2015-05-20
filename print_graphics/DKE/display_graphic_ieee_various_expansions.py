import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/*.json")
train_set = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 300, 553]


bow_ieee = {}
boc_ieee = {}
boc_ieee_expanded_09_09 = {}
boc_ieee_expanded_09_08 = {}
boc_ieee_expanded_08_09 = {}
boc_ieee_expanded_08_08 = {}

sys.stdout = open("Results/outputs/" + experiment_name + ".txt", 'w')

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow_ieee[int(json_data['train'])] = json_data['f1_score']
        elif json_data['expansion_threshold'] == None:
            boc_ieee[int(json_data['train'])] = json_data['f1_score']
        elif json_data['expansion_threshold'] != None:
            if json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.9:
                boc_ieee_expanded_09_09[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.8:
                boc_ieee_expanded_09_08[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.9:
                boc_ieee_expanded_08_09[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8:
                boc_ieee_expanded_08_08[int(json_data['train'])] = json_data['f1_score']
        print(json_data)

print ''
print ''

bow_ieee = sorted(bow_ieee.iteritems(), key=operator.itemgetter(1))
boc_ieee = sorted(boc_ieee.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_09_09 = sorted(boc_ieee_expanded_09_09.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_09_08 = sorted(boc_ieee_expanded_09_08.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_09 = sorted(boc_ieee_expanded_08_09.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08 = sorted(boc_ieee_expanded_08_08.iteritems(), key=operator.itemgetter(1))

print bow_ieee
print boc_ieee
print boc_ieee_expanded_09_09
print boc_ieee_expanded_09_08
print boc_ieee_expanded_08_09
print boc_ieee_expanded_08_08

p_bow, = plt.plot(train_set,  [x[1] for x in bow_ieee],'g*-')
p_boc, = plt.plot(train_set,  [x[1] for x in boc_ieee],'b.-')
p_boc_exp_09_09, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_09_09],'kx-')
p_boc_exp_09_08, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_09_08],'c*-')
p_boc_exp_08_09, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_09],'y.-')
p_boc_exp_08_08, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08],'mx-')
plt.legend([p_bow,p_boc,p_boc_exp_09_09,p_boc_exp_09_08,p_boc_exp_08_09,p_boc_exp_08_08], ["BoW", "BoC","BoC expanded_09_09","BoC expanded_09_08","BoC expanded_08_09","BoC expanded_08_08"], loc = "lower right")
#plt.show()
plt.savefig("Results/img/" + experiment_name)

