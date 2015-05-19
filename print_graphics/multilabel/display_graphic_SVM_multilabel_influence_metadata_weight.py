import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files = glob.glob("../../results/multilabel/" + experiment_folder + "/*.json")

metadata_weight = [0, 1, 2, 3, 8, 10, 13, 21, 25, 30, 34, 40, 55]

bow = {}
boc = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW":
            bow[int(json_data['metadata_weight'])] = json_data['f1_score']
        print(json_data)

print ''
print ''

bow = sorted(bow.iteritems(), key=operator.itemgetter(0))

print bow

p_bow, = plt.plot(metadata_weight, [x[1] for x in bow], 'ko-')

plt.title(experiment_folder)
plt.xlabel('metadata_frequency')
plt.ylabel('F1-score')
plt.legend([p_bow], ["BoW"], loc="lower right", prop={'size': 12})

plt.savefig("../../results/multilabel/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))
