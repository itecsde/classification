import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files = glob.glob("../../results/multilabel/" + experiment_folder + "/*.json")

train_set = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

bow_metadata = {}
bow_no_metadata = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['metadata_weight'] != 0:
            bow_metadata[int(json_data['train'])] = json_data['f1_score']
        elif json_data['metadata_weight'] == 0:
            bow_no_metadata[int(json_data['train'])] = json_data['f1_score']
        print(json_data)

print ''
print ''

bow_metadata = sorted(bow_metadata.iteritems(), key=operator.itemgetter(0))
bow_no_metadata = sorted(bow_no_metadata.iteritems(), key=operator.itemgetter(0))

print bow_metadata
print bow_no_metadata

p_bow_metadata, = plt.plot(train_set, [x[1] for x in bow_metadata], 'ko-')
p_bow_no_metadata, = plt.plot(train_set, [x[1] for x in bow_no_metadata], 'rx-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('F1-score')
plt.legend([p_bow_metadata, p_bow_no_metadata], ["With metadata", "Without metadata"], loc="lower right", prop={'size': 12})

plt.savefig("../../results/multilabel/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))