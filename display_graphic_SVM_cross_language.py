import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files =  glob.glob("Results/json/cross_language_SVM/" + experiment_folder +"/*.json")
#json_files = glob.glob("Results/json/Multilabel/" + experiment_folder + "/*.json")

train_set = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 2398]

bow = {}
boc = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow[int(json_data['train'])] = json_data['f1_score']
        elif json_data['representation'] == "BoC":
            boc[int(json_data['train'])] = json_data['f1_score']                                       
        print(json_data)

print ''
print ''

bow = sorted(bow.iteritems(), key=operator.itemgetter(0))
boc = sorted(boc.iteritems(), key=operator.itemgetter(0))


print bow
print boc


#p_bow, = plt.plot(train_set, [x[1] for x in bow], 'ko-')
p_boc, = plt.plot(train_set,  [x[1] for x in boc],'rx-')


plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('F1-score')
#plt.legend([p_bow,p_boc], ["BoW", "BoC"], loc = "lower right", prop={'size':12})
plt.legend([p_boc], ["BoC"], loc="lower right", prop={'size': 12})

plt.savefig("Results/json/cross_language_SVM/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))
# plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))
