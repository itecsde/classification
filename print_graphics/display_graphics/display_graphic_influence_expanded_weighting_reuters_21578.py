import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/experiment_influence_expanded_weighting_reuters_21578_0_8_0_8/*.json")


weighting_set = [0.001, 0.01, 0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

training_lenght_5 = {}
training_lenght_50 = {}
training_lenght_100 = {}
training_lenght_150 = {}

sys.stdout = open("Results/outputs/" + experiment_name + ".txt", 'w')

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['corpus'] == "reuters_21578_expanded":
            if json_data['train'] == 5:
                training_lenght_5[float(json_data['expanded_weighting'])] = json_data['f1_score']
            elif json_data['train'] == 50:
                training_lenght_50[float(json_data['expanded_weighting'])] = json_data['f1_score']
            elif json_data['train'] == 100:
                training_lenght_100[float(json_data['expanded_weighting'])] = json_data['f1_score']            
            elif json_data['train'] == 150:
                training_lenght_150[float(json_data['expanded_weighting'])] = json_data['f1_score']                            
            print(json_data)
print ''
print ''

training_lenght_5 = sorted(training_lenght_5.iteritems(), key=operator.itemgetter(0))
training_lenght_50 = sorted(training_lenght_50.iteritems(), key=operator.itemgetter(0))
training_lenght_100 = sorted(training_lenght_100.iteritems(), key=operator.itemgetter(0))
training_lenght_150 = sorted(training_lenght_150.iteritems(), key=operator.itemgetter(0))

print training_lenght_5
print training_lenght_50
print training_lenght_100
print training_lenght_150

p_training_lenght_5, = plt.plot(weighting_set, [x[1] for x in training_lenght_5],'gx-')
p_training_lenght_50, = plt.plot(weighting_set, [x[1] for x in training_lenght_50],'b*-')
p_training_lenght_100, = plt.plot(weighting_set, [x[1] for x in training_lenght_100],'r.-')
p_training_lenght_150, = plt.plot(weighting_set, [x[1] for x in training_lenght_150],'kx-')
plt.legend([p_training_lenght_5,p_training_lenght_50,p_training_lenght_100,p_training_lenght_150], ["Training Lenght = 5","Training Lenght = 50","Training Lenght = 100","Training Lenght = 150"], loc = "center right")
#plt.show()
plt.savefig("Results/img/" + experiment_name)
