import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_folder = sys.argv[1]

json_files =  glob.glob("Results/json/KNN/" + experiment_folder +"/*.json")
kbest_set = [100, 200, 300, 400, 500,1000,2000,5000]

bow_cosine = {}
bow_jaccard = {}
bow_braycurtis = {}
bow_euclidean = {}
bow_manhattan = {}
bow_chebyshev = {}

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
	corpus = json_data['corpus']
    if json_data['metric'] == "cosine":
    	bow_cosine[int(json_data['KBest'])] = json_data['f1_score']
    elif json_data['metric'] == "jaccard":
    	bow_jaccard[int(json_data['KBest'])] = json_data['f1_score']
    elif json_data['metric'] == "braycurtis":
    	bow_braycurtis[int(json_data['KBest'])] = json_data['f1_score']
    elif json_data['metric'] == "euclidean":
    	bow_euclidean[int(json_data['KBest'])] = json_data['f1_score']
    elif json_data['metric'] == "manhattan":
    	bow_manhattan[int(json_data['KBest'])] = json_data['f1_score']
    elif json_data['metric'] == "chebyshev":
    	bow_chebyshev[int(json_data['KBest'])] = json_data['f1_score']    	    	
           
    print(json_data)

print 
print





bow_cosine = sorted(bow_cosine.iteritems(), key=operator.itemgetter(0))
bow_jaccard = sorted(bow_jaccard.iteritems(), key=operator.itemgetter(0))
bow_braycurtis = sorted(bow_braycurtis.iteritems(), key=operator.itemgetter(0))
bow_euclidean = sorted(bow_euclidean.iteritems(), key=operator.itemgetter(0))
bow_manhattan = sorted(bow_manhattan.iteritems(), key=operator.itemgetter(0))
bow_chebyshev = sorted(bow_chebyshev.iteritems(), key=operator.itemgetter(0))


print bow_cosine
print bow_jaccard

p_bow_cosine, = plt.plot(kbest_set,  [x[1] for x in bow_cosine],'rx-')
p_bow_jaccard, = plt.plot(kbest_set,  [x[1] for x in bow_jaccard],'g.-')
p_bow_braycurtis, = plt.plot(kbest_set,  [x[1] for x in bow_braycurtis],'bo-')
p_bow_euclidean, = plt.plot(kbest_set,  [x[1] for x in bow_euclidean],'m*-')
p_bow_manhattan, = plt.plot(kbest_set,  [x[1] for x in bow_manhattan],'k+-')
p_bow_chebyshev, = plt.plot(kbest_set,  [x[1] for x in bow_chebyshev],'c3-')

plt.title(experiment_folder)
plt.xlabel('k')
plt.ylabel('F1-score')
plt.legend([p_bow_cosine, p_bow_jaccard, p_bow_braycurtis, p_bow_euclidean, p_bow_manhattan, p_bow_chebyshev], ["Cosine","Jaccard","BrayCurtis","Euclidean","Manhattan","Chebyshev"], loc = "lower right")

plt.savefig("Results/json/KNN/" + experiment_folder + "/" + experiment_folder.replace(".","_"))

