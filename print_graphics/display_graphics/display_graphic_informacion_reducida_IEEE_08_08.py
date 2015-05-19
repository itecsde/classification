import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/*.json")
#train_set = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 300, 553]
train_set = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150,300]


boc_ieee_expanded_08_08 = {}
boc_ieee_expanded_08_08_info_reducida_500 = {}
boc_ieee_expanded_08_08_info_reducida_250 = {}
boc_ieee_expanded_08_08_info_reducida_1000 = {}
boc_ieee_expanded_08_08_info_reducida_2000 = {}
boc_ieee_expanded_08_08_info_reducida_3000 = {}
boc_ieee_expanded_08_08_info_reducida_5000 = {}
boc_ieee_expanded_08_08_info_reducida_7000 = {}
boc_ieee_expanded_08_08_info_reducida_10000 = {}

#sys.stdout = open("Results/outputs/" + experiment_name + ".txt", 'w')

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
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 0 :
                boc_ieee_expanded_08_08[int(json_data['train'])] = json_data['f1_score']
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 500 :
                boc_ieee_expanded_08_08_info_reducida_500[int(json_data['train'])] = json_data['f1_score']     
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 250 :
                boc_ieee_expanded_08_08_info_reducida_250[int(json_data['train'])] = json_data['f1_score']                             
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 1000 :
                boc_ieee_expanded_08_08_info_reducida_1000[int(json_data['train'])] = json_data['f1_score']                     
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 2000 :
                boc_ieee_expanded_08_08_info_reducida_2000[int(json_data['train'])] = json_data['f1_score']            
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 3000 :
                boc_ieee_expanded_08_08_info_reducida_3000[int(json_data['train'])] = json_data['f1_score']    
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 5000 :
                boc_ieee_expanded_08_08_info_reducida_5000[int(json_data['train'])] = json_data['f1_score']    
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 7000 :
                boc_ieee_expanded_08_08_info_reducida_7000[int(json_data['train'])] = json_data['f1_score']    
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8 and json_data['KBest'] == 10000 :
                boc_ieee_expanded_08_08_info_reducida_10000[int(json_data['train'])] = json_data['f1_score']           
        print(json_data)

print ''
print ''

boc_ieee_expanded_08_08 = sorted(boc_ieee_expanded_08_08.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_500 = sorted(boc_ieee_expanded_08_08_info_reducida_500.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_250 = sorted(boc_ieee_expanded_08_08_info_reducida_250.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_1000 = sorted(boc_ieee_expanded_08_08_info_reducida_1000.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_2000 = sorted(boc_ieee_expanded_08_08_info_reducida_2000.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_3000 = sorted(boc_ieee_expanded_08_08_info_reducida_3000.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_5000 = sorted(boc_ieee_expanded_08_08_info_reducida_5000.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_7000 = sorted(boc_ieee_expanded_08_08_info_reducida_7000.iteritems(), key=operator.itemgetter(1))
boc_ieee_expanded_08_08_info_reducida_10000 = sorted(boc_ieee_expanded_08_08_info_reducida_10000.iteritems(), key=operator.itemgetter(1))

print boc_ieee_expanded_08_08
print boc_ieee_expanded_08_08_info_reducida_500
print boc_ieee_expanded_08_08_info_reducida_250
print boc_ieee_expanded_08_08_info_reducida_1000
print boc_ieee_expanded_08_08_info_reducida_2000
print boc_ieee_expanded_08_08_info_reducida_3000
print boc_ieee_expanded_08_08_info_reducida_5000
print boc_ieee_expanded_08_08_info_reducida_7000
print boc_ieee_expanded_08_08_info_reducida_10000

p_boc_exp_08_08, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08],'mx-')
#p_boc_exp_08_08_info_reducida_250, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_250],'bx-')
#p_boc_exp_08_08_info_reducida_500, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_500],'g*-')
#p_boc_exp_08_08_info_reducida_1000, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_1000],'k.-')
#p_boc_exp_08_08_info_reducida_2000, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_2000],'y+-')
p_boc_exp_08_08_info_reducida_3000, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_3000],'bx-')
p_boc_exp_08_08_info_reducida_5000, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_5000],'g*-')
p_boc_exp_08_08_info_reducida_7000, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_7000],'k.-')
p_boc_exp_08_08_info_reducida_10000, = plt.plot(train_set, [x[1] for x in boc_ieee_expanded_08_08_info_reducida_10000],'y+-')

#plt.legend([p_boc_exp_08_08, p_boc_exp_08_08_info_reducida_500], ["BoC expanded_08_08","BoC expanded_08_08_info_reducida_500"], loc = "lower right")

#plt.legend([p_boc_exp_08_08, p_boc_exp_08_08_info_reducida_250, p_boc_exp_08_08_info_reducida_500, p_boc_exp_08_08_info_reducida_1000, p_boc_exp_08_08_info_reducida_2000], ["BoC expanded_08_08","BoC expanded_08_08_info_reducida_250","BoC expanded_08_08_info_reducida_500","BoC expanded_08_08_info_reducida_1000","BoC expanded_08_08_info_reducida_2000"], loc = "lower right")

plt.legend([p_boc_exp_08_08,p_boc_exp_08_08_info_reducida_3000, p_boc_exp_08_08_info_reducida_5000, p_boc_exp_08_08_info_reducida_7000, p_boc_exp_08_08_info_reducida_10000], ["BoC expanded_08_08","BoC expanded_08_08_info_reducida_3000","BoC expanded_08_08_info_reducida_5000","BoC expanded_08_08_info_reducida_7000","BoC expanded_08_08_info_reducida_10000"], loc = "lower right")

#plt.show()
plt.savefig("Results/img/" + experiment_name)







