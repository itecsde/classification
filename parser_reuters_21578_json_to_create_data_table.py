import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

json_files =  glob.glob("Results/json/Reuters_21578_BoW_BoC_BoC_various_expansions/*.json")

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


for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow_reuters_21578[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
        elif json_data['expansion_threshold'] == None:
            boc_reuters_21578[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
        elif json_data['expansion_threshold'] != None:
            if json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.9:
                boc_reuters_21578_expanded_09_09[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.8:
                boc_reuters_21578_expanded_09_08[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.9:
                boc_reuters_21578_expanded_08_09[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.8:
                boc_reuters_21578_expanded_08_08[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.7 and json_data['expansion_relatedness'] == 0.7:
                boc_reuters_21578_expanded_07_07[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.8 and json_data['expansion_relatedness'] == 0.7:
                boc_reuters_21578_expanded_08_07[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.7 and json_data['expansion_relatedness'] == 0.8:
                boc_reuters_21578_expanded_07_08[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])   
            elif json_data['expansion_threshold'] == 0.9 and json_data['expansion_relatedness'] == 0.7:
                boc_reuters_21578_expanded_09_07[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])
            elif json_data['expansion_threshold'] == 0.7 and json_data['expansion_relatedness'] == 0.9:
                boc_reuters_21578_expanded_07_09[int(json_data['train'])] = '%.3f'%(json_data['f1_score'])                                               
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

print "BoW"
print bow_reuters_21578
print "BoC"
print boc_reuters_21578
print "Expanded BoC 0.9-0.9"
print boc_reuters_21578_expanded_09_09
print "Expanded BoC 0.9-0.8"
print boc_reuters_21578_expanded_09_08
print "Expanded BoC 0.8-0.9"
print boc_reuters_21578_expanded_08_09
print "Expanded BoC 0.8-0.8"
print boc_reuters_21578_expanded_08_08
print "Expanded BoC 0.7-0.7"
print boc_reuters_21578_expanded_07_07
print "Expanded BoC 0.7-0.8"
print boc_reuters_21578_expanded_07_08
print "Expanded BoC 0.8-0.7"
print boc_reuters_21578_expanded_08_07
print "Expanded BoC 0.7-0.9"
print boc_reuters_21578_expanded_07_09
print "Expanded BoC 0.9-0.7"
print boc_reuters_21578_expanded_09_07


