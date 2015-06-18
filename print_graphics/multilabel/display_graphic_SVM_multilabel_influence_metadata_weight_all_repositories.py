import glob
import matplotlib.pyplot as plt
import json
import operator
import sys

experiment_folder = sys.argv[1]

print "exp folder"
print experiment_folder

json_files = glob.glob("../../results/multilabel/" + experiment_folder + "/*.json")

metadata_weight = [0, 1, 2, 3, 8, 10, 13, 21, 25]

bow_oercommons = {}
bow_merlot = {}
bow_cnx = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['representation'] == "BoW" and json_data['corpus'] == "oercommons":
            bow_oercommons[int(json_data['metadata_weight'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW" and json_data['corpus'] == "merlot":
            bow_merlot[int(json_data['metadata_weight'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW" and json_data['corpus'] == "cnx":
            bow_cnx[int(json_data['metadata_weight'])] = json_data['f1_score']
        print(json_data)

print ''
print ''

bow_oercommons = sorted(bow_oercommons.iteritems(), key=operator.itemgetter(0))
bow_merlot = sorted(bow_merlot.iteritems(), key=operator.itemgetter(0))
bow_cnx = sorted(bow_cnx.iteritems(), key=operator.itemgetter(0))

print bow_oercommons
print bow_merlot
print bow_cnx

p_bow_oercommons, = plt.plot(metadata_weight, [x[1] for x in bow_oercommons], 'ko-')
p_bow_merlot, = plt.plot(metadata_weight, [x[1] for x in bow_merlot], 'rx-')
p_bow_cnx, = plt.plot(metadata_weight, [x[1] for x in bow_cnx], 'b*-')

plt.title(experiment_folder)
plt.xlabel('metadata_frequency')
plt.ylabel('F1-score')
plt.legend([p_bow_oercommons, p_bow_merlot, p_bow_cnx], ["OERCommons", "MERLOT" ,"Open Stax CNX"], loc="lower right", prop={'size': 12})

plt.savefig("../../results/multilabel/" + experiment_folder + "/" + experiment_folder.replace(".", "_"))
