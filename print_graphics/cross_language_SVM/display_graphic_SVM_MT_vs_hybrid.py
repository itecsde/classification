import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files =  glob.glob("../../results/cross_language_SVM/" + experiment_folder +"/*.json")

train_set = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

bow = {}
cl = {}
hybrid = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        print json_data
        if json_data['representation'] == "BoW" and json_data['hybrid'] == "yes":
            hybrid[int(json_data['train'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW" and json_data['hybrid'] == "no":
            bow[int(json_data['train'])] = json_data['f1_score']
        elif json_data['representation'] == "BoC":
            cl[int(json_data['train'])] = json_data['f1_score']
        print(json_data)

print ''
print ''

bow = sorted(bow.iteritems(), key=operator.itemgetter(0))
cl = sorted(cl.iteritems(), key=operator.itemgetter(0))
hybrid = sorted(hybrid.iteritems(), key=operator.itemgetter(0))

print bow
print cl
print hybrid

p_bow, = plt.plot(train_set, [x[1] for x in bow], 'ko-')
p_cl, = plt.plot(train_set,  [x[1] for x in cl],'b.-')
p_hybrid, = plt.plot(train_set,  [x[1] for x in hybrid],'rx-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('F1-score')

plt.legend([p_bow,p_hybrid, p_cl], ["BoW + MT", "Hybrid model", "BoC + CLCM"], loc = "lower right", prop={'size':12})

#plt.show

plt.savefig("../../results/cross_language_SVM/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))
