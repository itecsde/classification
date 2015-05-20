import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_folder = sys.argv[1]

json_files =  glob.glob("Results/json/Multilabel/" + experiment_folder +"/*.json")

#training_sequence = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 11000, 12000, 13000, 14000]
training_sequence = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
##test_sequence = [100, 200, 500, 1000, 2000]
#test_sequence = [100, 200, 500, 1000, 2000, 5000]

test_sequence = [1000]

f1_bow_svc = {}
f1_bow_bayes = {}
f1_bow_knn = {}
f1_bow_sgd = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        corpus = json_data['corpus']
        if 'expanded' in json_data['corpus']:
            boc_expanded[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoC":
            boc[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW":
            if json_data['algorithm'] == "SVC":
                f1_bow_svc[int(json_data['train'])] = json_data['f1_score']

            elif json_data['algorithm'] == "Bayes":
                f1_bow_bayes[int(json_data['train'])] = json_data['f1_score']

            elif json_data['algorithm'] == "KNN":
                f1_bow_knn[int(json_data['train'])] = json_data['f1_score']

            elif json_data['algorithm'] == "SGD":
                f1_bow_sgd[int(json_data['train'])] = json_data['f1_score']
            
           
        print(json_data)

print 
print


f1_bow_svc = sorted(f1_bow_svc.iteritems(), key=operator.itemgetter(0))
f1_bow_bayes = sorted(f1_bow_bayes.iteritems(), key=operator.itemgetter(0))
f1_bow_knn = sorted(f1_bow_knn.iteritems(), key=operator.itemgetter(0))
f1_bow_sgd = sorted(f1_bow_sgd.iteritems(), key=operator.itemgetter(0))


''' F1 GRAPHIC '''

f1_p_bow_svc, = plt.plot(training_sequence,  [x[1] for x in f1_bow_svc],'bo-')
f1_p_bow_bayes, = plt.plot(training_sequence,  [x[1] for x in f1_bow_bayes],'r*-')
f1_p_bow_knn, = plt.plot(training_sequence,  [x[1] for x in f1_bow_knn],'gx-')
f1_p_bow_sgd, = plt.plot(training_sequence,  [x[1] for x in f1_bow_sgd],'k.-')


plt.title("OHSUMED")
plt.xlabel('Training sequence')
plt.ylabel('F1-score')

plt.legend([f1_p_bow_svc, f1_p_bow_bayes, f1_p_bow_knn, f1_p_bow_sgd], ["SVC","Naive Bayes","KNN","SGD"], loc = "upper left")
plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + (experiment_folder + "_F1").replace(".","_"))