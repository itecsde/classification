import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/Reuters_21578_BoW_BoC_BoC_various_expansions/*.json")
train_set = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150]


bow_reuters_21578 = {}
boc_reuters_21578 = {}
boc_reuters_21578_expanded_09_09 = {}
boc_reuters_21578_expanded_09_08 = {}
boc_reuters_21578_expanded_08_09 = {}
boc_reuters_21578_expanded_08_08 = {}
boc_reuters_21578_expanded_07_07 = {}
boc_reuters_21578_expanded_07_08 = {}
boc_reuters_21578_expanded_08_07 = {}
boc_reuters_21578_expanded_07_09 = {}
boc_reuters_21578_expanded_09_07 = {}

sys.stdout = open("Results/outputs/" + experiment_name + ".txt", 'w')

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow_reuters_21578[int(json_data['train'])] = json_data['f1_score']
        elif json_data['expansion_threshold'] == None:
            boc_reuters_21578[int(json_data['train'])] = json_data['f1_score']
        elif json_data['expansion_threshold'] != None:
            if json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.9:
                boc_reuters_21578_expanded_09_09[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.8:
                boc_reuters_21578_expanded_09_08[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.9:
                boc_reuters_21578_expanded_08_09[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8:
                boc_reuters_21578_expanded_08_08[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.7 and json_data['expansion_relatedness'] == 0.7:
                boc_reuters_21578_expanded_07_07[int(json_data['train'])] = json_data['f1_score']  
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.7:
                boc_reuters_21578_expanded_08_07[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.7 and json_data['expansion_relatedness'] == 0.8:
                boc_reuters_21578_expanded_07_08[int(json_data['train'])] = json_data['f1_score']   
            elif json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.7:
                boc_reuters_21578_expanded_09_07[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.7 and json_data['expansion_relatedness'] == 0.9:
                boc_reuters_21578_expanded_07_09[int(json_data['train'])] = json_data['f1_score']                                               
        print(json_data)

print ''
print ''

bow_reuters_21578 = sorted(bow_reuters_21578.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578 = sorted(boc_reuters_21578.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_09_09 = sorted(boc_reuters_21578_expanded_09_09.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_09_08 = sorted(boc_reuters_21578_expanded_09_08.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_08_09 = sorted(boc_reuters_21578_expanded_08_09.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_08_08 = sorted(boc_reuters_21578_expanded_08_08.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_07_07 = sorted(boc_reuters_21578_expanded_07_07.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_08_07 = sorted(boc_reuters_21578_expanded_08_07.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_07_08 = sorted(boc_reuters_21578_expanded_07_08.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_09_07 = sorted(boc_reuters_21578_expanded_09_07.iteritems(), key=operator.itemgetter(0))
boc_reuters_21578_expanded_07_09 = sorted(boc_reuters_21578_expanded_07_09.iteritems(), key=operator.itemgetter(0))

print bow_reuters_21578
print boc_reuters_21578
print boc_reuters_21578_expanded_09_09
print boc_reuters_21578_expanded_09_08
print boc_reuters_21578_expanded_08_09
print boc_reuters_21578_expanded_08_08
print boc_reuters_21578_expanded_07_07
print boc_reuters_21578_expanded_07_08
print boc_reuters_21578_expanded_08_07
print boc_reuters_21578_expanded_07_09
print boc_reuters_21578_expanded_09_07

p_bow, = plt.plot(train_set,  [x[1] for x in bow_reuters_21578],'g*-')
p_boc, = plt.plot(train_set,  [x[1] for x in boc_reuters_21578],'b.-')
#p_boc_exp_09_09, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_09_09],'kx-')
#p_boc_exp_09_08, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_09_08],'c*-')
#p_boc_exp_08_09, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_08_09],'y.-')
#p_boc_exp_08_08, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_08_08],'mx-')
p_boc_exp_07_07, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_07_07],'mx-')
#p_boc_exp_08_07, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_08_07],'g+-')
#p_boc_exp_07_08, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_07_08],'b*-')
#p_boc_exp_09_07, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_09_07],'k.-')
#p_boc_exp_07_09, = plt.plot(train_set, [x[1] for x in boc_reuters_21578_expanded_07_09],'rx-')

#plt.legend([p_bow,p_boc,p_boc_exp_09_09,p_boc_exp_09_08,p_boc_exp_08_09,p_boc_exp_09_07,p_boc_exp_07_09,p_boc_exp_08_08,p_boc_exp_08_07,p_boc_exp_07_08,p_boc_exp_07_07,], ["BoW", "BoC","BoC expanded_09_09","BoC expanded_09_08","BoC expanded_08_09","BoC expanded_09_07","BoC expanded_07_09","BoC expanded_08_08","BoC expanded_08_07","BoC expanded_07_08","BoC expanded_07_07"], loc = "lower right", prop={'size':9})



plt.legend([p_bow,p_boc,p_boc_exp_07_07], ["BoW", "BoC","BoC expanded_07_07"], loc = "lower right", prop={'size':12})
#plt.legend([p_bow,p_boc,p_boc_exp_09_09,p_boc_exp_08_08,p_boc_exp_07_07], ["BoW", "BoC","BoC expanded_09_09","BoC expanded_08_08","BoC expanded_07_07"], loc = "lower right")
#plt.legend([p_boc_exp_09_09,p_boc_exp_08_08,p_boc_exp_07_07], ["BoC expanded_09_09","BoC expanded_08_08","BoC expanded_07_07"], loc = "lower right")
#plt.legend([p_boc_exp_08_08,p_boc_exp_08_09,p_boc_exp_09_08,p_boc_exp_07_08,p_boc_exp_08_07,p_boc_exp_09_07,p_boc_exp_07_09], ["BoC expanded_08_08","BoC expanded_08_09","BoC expanded_09_08","BoC expanded_07_08","BoC expanded_08_07","BoC expanded_09_07","BoC expanded_07_09"], loc = "lower right")


#plt.show()
plt.savefig("Results/img/" + experiment_name)

