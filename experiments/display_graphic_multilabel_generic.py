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

f1_bow_100_test = {}
accuracy_bow_100_test = {}
precision_bow_100_test = {}
hamming_loss_bow_100_test = {}
recall_bow_100_test = {}

f1_bow_200_test = {}
accuracy_bow_200_test = {}
precision_bow_200_test = {}
hamming_loss_bow_200_test = {}
recall_bow_200_test = {}

f1_bow_500_test = {}
accuracy_bow_500_test = {}
precision_bow_500_test = {}
hamming_loss_bow_500_test = {}
recall_bow_500_test = {}

f1_bow_1000_test = {}
accuracy_bow_1000_test = {}
precision_bow_1000_test = {}
hamming_loss_bow_1000_test = {}
recall_bow_1000_test = {}

f1_bow_2000_test = {}
accuracy_bow_2000_test = {}
precision_bow_2000_test = {}
hamming_loss_bow_2000_test = {}
recall_bow_2000_test = {}

f1_bow_5000_test = {}
accuracy_bow_5000_test = {}
precision_bow_5000_test = {}
hamming_loss_bow_5000_test = {}
recall_bow_5000_test = {}



for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        corpus = json_data['corpus']
        if 'expanded' in json_data['corpus']:
            boc_expanded[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoC":
            boc[int(json_data['n_neighbors'])] = json_data['f1_score']
        elif json_data['representation'] == "BoW":
            if json_data['test'] == 100:
                f1_bow_100_test[int(json_data['train'])] = json_data['f1_score']
                accuracy_bow_100_test[int(json_data['train'])] = json_data['accuracy']
                precision_bow_100_test[int(json_data['train'])] = json_data['precision']
                hamming_loss_bow_100_test[int(json_data['train'])] = json_data['hamming_loss']
                recall_bow_100_test[int(json_data['train'])] = json_data['recall']

            elif json_data['test'] == 200:
                f1_bow_200_test[int(json_data['train'])] = json_data['f1_score']
                accuracy_bow_200_test[int(json_data['train'])] = json_data['accuracy']
                precision_bow_200_test[int(json_data['train'])] = json_data['precision']
                hamming_loss_bow_200_test[int(json_data['train'])] = json_data['hamming_loss']
                recall_bow_200_test[int(json_data['train'])] = json_data['recall']

            elif json_data['test'] == 500:
                f1_bow_500_test[int(json_data['train'])] = json_data['f1_score']
                accuracy_bow_500_test[int(json_data['train'])] = json_data['accuracy']
                precision_bow_500_test[int(json_data['train'])] = json_data['precision']
                hamming_loss_bow_500_test[int(json_data['train'])] = json_data['hamming_loss']
                recall_bow_500_test[int(json_data['train'])] = json_data['recall']

            elif json_data['test'] == 1000:
                f1_bow_1000_test[int(json_data['train'])] = json_data['f1_score']
                accuracy_bow_1000_test[int(json_data['train'])] = json_data['accuracy']
                precision_bow_1000_test[int(json_data['train'])] = json_data['precision']
                hamming_loss_bow_1000_test[int(json_data['train'])] = json_data['hamming_loss']
                recall_bow_1000_test[int(json_data['train'])] = json_data['recall']   

            elif json_data['test'] == 2000:
                f1_bow_2000_test[int(json_data['train'])] = json_data['f1_score']
                accuracy_bow_2000_test[int(json_data['train'])] = json_data['accuracy']
                precision_bow_2000_test[int(json_data['train'])] = json_data['precision']
                hamming_loss_bow_2000_test[int(json_data['train'])] = json_data['hamming_loss']
                recall_bow_2000_test[int(json_data['train'])] = json_data['recall']              
            
            elif json_data['test'] == 5000:
                f1_bow_5000_test[int(json_data['train'])] = json_data['f1_score']
                accuracy_bow_5000_test[int(json_data['train'])] = json_data['accuracy']
                precision_bow_5000_test[int(json_data['train'])] = json_data['precision']
                hamming_loss_bow_5000_test[int(json_data['train'])] = json_data['hamming_loss']
                recall_bow_5000_test[int(json_data['train'])] = json_data['recall']              
            
           
        print(json_data)

print 
print

'''
f1_bow_100_test = sorted(f1_bow_100_test.iteritems(), key=operator.itemgetter(0))
accuracy_bow_100_test = sorted(accuracy_bow_100_test.iteritems(), key=operator.itemgetter(0))
precision_bow_100_test = sorted(precision_bow_100_test.iteritems(), key=operator.itemgetter(0))
hamming_loss_bow_100_test = sorted(hamming_loss_bow_100_test.iteritems(), key=operator.itemgetter(0))
recall_bow_100_test = sorted(recall_bow_100_test.iteritems(), key=operator.itemgetter(0))

f1_bow_200_test = sorted(f1_bow_200_test.iteritems(), key=operator.itemgetter(0))
accuracy_bow_200_test = sorted(accuracy_bow_200_test.iteritems(), key=operator.itemgetter(0))
precision_bow_200_test = sorted(precision_bow_200_test.iteritems(), key=operator.itemgetter(0))
hamming_loss_bow_200_test = sorted(hamming_loss_bow_200_test.iteritems(), key=operator.itemgetter(0))
recall_bow_200_test = sorted(recall_bow_200_test.iteritems(), key=operator.itemgetter(0))

f1_bow_500_test = sorted(f1_bow_500_test.iteritems(), key=operator.itemgetter(0))
accuracy_bow_500_test = sorted(accuracy_bow_500_test.iteritems(), key=operator.itemgetter(0))
precision_bow_500_test = sorted(precision_bow_500_test.iteritems(), key=operator.itemgetter(0))
hamming_loss_bow_500_test = sorted(hamming_loss_bow_500_test.iteritems(), key=operator.itemgetter(0))
recall_bow_500_test = sorted(recall_bow_500_test.iteritems(), key=operator.itemgetter(0))
'''
f1_bow_1000_test = sorted(f1_bow_1000_test.iteritems(), key=operator.itemgetter(0))
accuracy_bow_1000_test = sorted(accuracy_bow_1000_test.iteritems(), key=operator.itemgetter(0))
precision_bow_1000_test = sorted(precision_bow_1000_test.iteritems(), key=operator.itemgetter(0))
hamming_loss_bow_1000_test = sorted(hamming_loss_bow_1000_test.iteritems(), key=operator.itemgetter(0))
recall_bow_1000_test = sorted(recall_bow_1000_test.iteritems(), key=operator.itemgetter(0))
'''
f1_bow_2000_test = sorted(f1_bow_2000_test.iteritems(), key=operator.itemgetter(0))
accuracy_bow_2000_test = sorted(accuracy_bow_2000_test.iteritems(), key=operator.itemgetter(0))
precision_bow_2000_test = sorted(precision_bow_2000_test.iteritems(), key=operator.itemgetter(0))
hamming_loss_bow_2000_test = sorted(hamming_loss_bow_2000_test.iteritems(), key=operator.itemgetter(0))
recall_bow_2000_test = sorted(recall_bow_2000_test.iteritems(), key=operator.itemgetter(0))

f1_bow_5000_test = sorted(f1_bow_5000_test.iteritems(), key=operator.itemgetter(0))
accuracy_bow_5000_test = sorted(accuracy_bow_5000_test.iteritems(), key=operator.itemgetter(0))
precision_bow_5000_test = sorted(precision_bow_5000_test.iteritems(), key=operator.itemgetter(0))
hamming_loss_bow_5000_test = sorted(hamming_loss_bow_5000_test.iteritems(), key=operator.itemgetter(0))
recall_bow_5000_test = sorted(recall_bow_5000_test.iteritems(), key=operator.itemgetter(0))
'''


''' F1 GRAPHIC '''
#f1_p_bow_100_test, = plt.plot(training_sequence,  [x[1] for x in f1_bow_100_test],'rx-')
#f1_p_bow_200_test, = plt.plot(training_sequence,  [x[1] for x in f1_bow_200_test],'g*-')
#f1_p_bow_500_test, = plt.plot(training_sequence,  [x[1] for x in f1_bow_500_test],'c.-')
f1_p_bow_1000_test, = plt.plot(training_sequence,  [x[1] for x in f1_bow_1000_test],'b+-')
#f1_p_bow_2000_test, = plt.plot(training_sequence,  [x[1] for x in f1_bow_2000_test],'ko-')
#f1_p_bow_5000_test, = plt.plot(training_sequence,  [x[1] for x in f1_bow_5000_test],'m3-')


plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('F1-score')

#plt.legend([f1_p_bow_100_test, f1_p_bow_200_test, f1_p_bow_500_test, f1_p_bow_1000_test, f1_p_bow_2000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test",], loc = "lower right")
#plt.legend([f1_p_bow_100_test, f1_p_bow_200_test, f1_p_bow_500_test, f1_p_bow_1000_test, f1_p_bow_2000_test, f1_p_bow_5000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test","BoW 5000 test"], loc = "lower right")
plt.legend([f1_p_bow_1000_test], ["BoW 1000 test"], loc = "lower right")
plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + (experiment_folder + "_F1").replace(".","_"))
plt.clf()


''' ACCURACY GRAPHIC '''
#accuracy_p_bow_100_test, = plt.plot(training_sequence,  [x[1] for x in accuracy_bow_100_test],'rx-')
#accuracy_p_bow_200_test, = plt.plot(training_sequence,  [x[1] for x in accuracy_bow_200_test],'g*-')
#accuracy_p_bow_500_test, = plt.plot(training_sequence,  [x[1] for x in accuracy_bow_500_test],'c.-')
accuracy_p_bow_1000_test, = plt.plot(training_sequence,  [x[1] for x in accuracy_bow_1000_test],'b+-')
#accuracy_p_bow_2000_test, = plt.plot(training_sequence,  [x[1] for x in accuracy_bow_2000_test],'ko-')
#accuracy_p_bow_5000_test, = plt.plot(training_sequence,  [x[1] for x in accuracy_bow_5000_test],'m3-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('Accuracy')

#plt.legend([accuracy_p_bow_100_test, accuracy_p_bow_200_test,accuracy_p_bow_500_test, accuracy_p_bow_1000_test, accuracy_p_bow_2000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test",], loc = "lower right")
#plt.legend([accuracy_p_bow_100_test, accuracy_p_bow_200_test,accuracy_p_bow_500_test, accuracy_p_bow_1000_test, accuracy_p_bow_2000_test, accuracy_p_bow_5000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test","BoW 5000 test"], loc = "lower right")
plt.legend([accuracy_p_bow_1000_test], ["BoW 1000 test"], loc = "lower right")
plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + (experiment_folder + "_accuracy").replace(".","_"))
plt.clf()

''' PRECISION GRAPHIC '''
#precision_p_bow_100_test, = plt.plot(training_sequence,  [x[1] for x in precision_bow_100_test],'rx-')
#precision_p_bow_200_test, = plt.plot(training_sequence,  [x[1] for x in precision_bow_200_test],'g*-')
#precision_p_bow_500_test, = plt.plot(training_sequence,  [x[1] for x in precision_bow_500_test],'c.-')
precision_p_bow_1000_test, = plt.plot(training_sequence,  [x[1] for x in precision_bow_1000_test],'b+-')
#precision_p_bow_2000_test, = plt.plot(training_sequence,  [x[1] for x in precision_bow_2000_test],'ko-')
#precision_p_bow_5000_test, = plt.plot(training_sequence,  [x[1] for x in precision_bow_5000_test],'m3-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('Precision')

#plt.legend([precision_p_bow_100_test, precision_p_bow_200_test, precision_p_bow_500_test, precision_p_bow_1000_test, precision_p_bow_2000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test",], loc = "lower right")
#plt.legend([precision_p_bow_100_test, precision_p_bow_200_test, precision_p_bow_500_test, precision_p_bow_1000_test, precision_p_bow_2000_test,precision_p_bow_5000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test","BoW 5000 test"], loc = "lower right")
plt.legend([precision_p_bow_1000_test], ["BoW 1000 test"], loc = "lower right")
plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + (experiment_folder + "_precision").replace(".","_"))
plt.clf()

''' HAMMING_LOSS GRAPHIC '''
#hamming_loss_p_bow_100_test, = plt.plot(training_sequence,  [x[1] for x in hamming_loss_bow_100_test],'rx-')
#hamming_loss_p_bow_200_test, = plt.plot(training_sequence,  [x[1] for x in hamming_loss_bow_200_test],'g*-')
#hamming_loss_p_bow_500_test, = plt.plot(training_sequence,  [x[1] for x in hamming_loss_bow_500_test],'c.-')
hamming_loss_p_bow_1000_test, = plt.plot(training_sequence,  [x[1] for x in hamming_loss_bow_1000_test],'b+-')
#hamming_loss_p_bow_2000_test, = plt.plot(training_sequence,  [x[1] for x in hamming_loss_bow_2000_test],'ko-')
#hamming_loss_p_bow_5000_test, = plt.plot(training_sequence,  [x[1] for x in hamming_loss_bow_5000_test],'m3-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('Hamming Loss')

#plt.legend([hamming_loss_p_bow_100_test, hamming_loss_p_bow_200_test, hamming_loss_p_bow_500_test, hamming_loss_p_bow_1000_test, hamming_loss_p_bow_2000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test",], loc = "upper right")
#plt.legend([hamming_loss_p_bow_100_test, hamming_loss_p_bow_200_test, hamming_loss_p_bow_500_test, hamming_loss_p_bow_1000_test, hamming_loss_p_bow_2000_test, hamming_loss_p_bow_5000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test", "BoW 5000 test"], loc = "upper right")
plt.legend([hamming_loss_p_bow_1000_test], ["BoW 1000 test"], loc = "upper right")
plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + (experiment_folder + "_hamming_loss").replace(".","_"))
plt.clf()

''' RECALL GRAPHIC '''
#recall_p_bow_100_test, = plt.plot(training_sequence,  [x[1] for x in recall_bow_100_test],'rx-')
#recall_p_bow_200_test, = plt.plot(training_sequence,  [x[1] for x in recall_bow_200_test],'g*-')
#recall_p_bow_500_test, = plt.plot(training_sequence,  [x[1] for x in recall_bow_500_test],'c.-')
recall_p_bow_1000_test, = plt.plot(training_sequence,  [x[1] for x in recall_bow_1000_test],'b+-')
#recall_p_bow_2000_test, = plt.plot(training_sequence,  [x[1] for x in recall_bow_2000_test],'ko-')
#recall_p_bow_5000_test, = plt.plot(training_sequence,  [x[1] for x in recall_bow_5000_test],'m3-')

plt.title(experiment_folder)
plt.xlabel('Training sequence')
plt.ylabel('Recall')

#plt.legend([recall_p_bow_100_test, recall_p_bow_200_test, recall_p_bow_500_test, recall_p_bow_1000_test, recall_p_bow_2000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test",], loc = "lower right")
#plt.legend([recall_p_bow_100_test, recall_p_bow_200_test, recall_p_bow_500_test, recall_p_bow_1000_test, recall_p_bow_2000_test, recall_p_bow_5000_test], ["BoW 100 test","BoW 200 test","BoW 500 test","BoW 1000 test","BoW 2000 test","BoW 5000 test"], loc = "lower right")
plt.legend([recall_p_bow_1000_test], ["BoW 1000 test"], loc = "lower right")
plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + (experiment_folder + "_recall").replace(".","_"))

