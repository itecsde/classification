import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 
experiment_name = sys.argv[1]

#json_files =  glob.glob("/media/almacen/Dropbox/Concept-Based_Paradigm/Classification/Results/json/*.json")
json_files =  glob.glob("Results/json/*.json")

smoothing_set = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5]


training_lenght_150_20NG = {}
training_lenght_150_ohsumed = {}
training_lenght_100_ieee = {}

sys.stdout = open("Results/outputs/" + experiment_name + ".txt", 'w')

for file in json_files:
    with open(file) as json_file:
        json_data = json.load(json_file)
        if json_data['corpus'] == "20_newsgroup":
            if json_data['train'] == 150:
                training_lenght_150_20NG[float(json_data['smoothing'])] = json_data['f1_score']                            
        elif json_data['corpus'] == "ohsumed":
            if json_data['train'] == 150:
                training_lenght_150_ohsumed[float(json_data['smoothing'])] = json_data['f1_score']                    
        elif json_data['corpus'] == "ieee":
            if json_data['train'] == 100:
                training_lenght_100_ieee[float(json_data['smoothing'])] = json_data['f1_score']                    
            print(json_data)
print ''
print ''

training_lenght_150_20NG = sorted(training_lenght_150_20NG.iteritems(), key=operator.itemgetter(0))
training_lenght_150_ohsumed = sorted(training_lenght_150_ohsumed.iteritems(), key=operator.itemgetter(0))
training_lenght_100_ieee = sorted(training_lenght_100_ieee.iteritems(), key=operator.itemgetter(0))

print training_lenght_150_20NG
print training_lenght_150_ohsumed
print training_lenght_100_ieee

p_training_lenght_150_20NG, = plt.plot(smoothing_set, [x[1] for x in training_lenght_150_20NG],'kx-')
p_training_lenght_150_ohsumed, = plt.plot(smoothing_set, [x[1] for x in training_lenght_150_ohsumed],'g*-')
p_training_lenght_100_ieee, = plt.plot(smoothing_set, [x[1] for x in training_lenght_100_ieee],'b.-')

plt.legend([p_training_lenght_150_20NG,p_training_lenght_150_ohsumed, p_training_lenght_100_ieee], ["20NG, training Lenght = 150","ohsumed, training Lenght = 150","ieee, training Lenght = 100"], loc = "lower right")
#plt.show()
plt.savefig("Results/img/" + experiment_name)
