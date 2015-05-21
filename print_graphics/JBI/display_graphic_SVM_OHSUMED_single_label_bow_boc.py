import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files =  glob.glob("Results/json/SVM/" + experiment_folder +"/*.json")

train_set = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150,300, 500, 750, 1000]
train_set = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]


bow_ohsumed = {}
boc_ohsumed = {}


for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow_ohsumed[int(json_data['train'])] = json_data['f1_score']
        elif json_data['representation'] == "BoC":
            boc_ohsumed[int(json_data['train'])] = json_data['f1_score']                                       
        print(json_data)

print ''
print ''

bow_ohsumed = sorted(bow_ohsumed.iteritems(), key=operator.itemgetter(0))
boc_ohsumed = sorted(boc_ohsumed.iteritems(), key=operator.itemgetter(0))


print bow_ohsumed
print boc_ohsumed


p_bow, = plt.plot(train_set,  [x[1] for x in bow_ohsumed],'rx-')
p_boc, = plt.plot(train_set,  [x[1] for x in boc_ohsumed],'ko-')


plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('F1-score')
plt.legend([p_bow,p_boc], ["BoW", "BoC"], loc = "lower right", prop={'size':12})

plt.savefig("Results/json/SVM/" + experiment_folder + "/" + experiment_folder.replace(".","_"))
