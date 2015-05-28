import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files =  glob.glob("../../results/cross_language_SVM/" + experiment_folder +"/*.json")

kbest = [10, 20, 50, 70, 100, 200, 500, 700, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000]

boc = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoC":
            boc[int(json_data['KBest'])] = json_data['f1_score']
        print(json_data)

print ''
print ''

boc = sorted(boc.iteritems(), key=operator.itemgetter(0))

print boc

p_boc, = plt.plot(kbest,  [x[1] for x in boc],'rx-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('F1-score')
plt.legend([p_boc], ["BoC"], loc = "lower right", prop={'size':12})

plt.savefig("../../results/cross_language_SVM/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))
