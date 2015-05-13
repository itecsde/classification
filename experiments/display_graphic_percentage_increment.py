import glob
import matplotlib.pyplot as plt
import json
import operator
import sys
 


train_set = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]




uvigomed_sl = [(5,-34.6153846154),(10,48.1481481481),(20,122.8571428571),(50,90.1639344262),(100,113.0952380952),(200,97.7941176471),(500,50.4545454545),(1000,37.8091872792),(2000,19.4444444444),(5000,10.9263657957)]


uvigomed_ml = [(5,-60),(10,-23.0769230769),(20,21.4285714286),(50,40),(100,155.1724137931),(200,112.5),(500,79.3333333333),(1000,52.466367713),(2000,19.9356913183),(5000,5.9585492228)]

							

ohsumed_sl = [(5,7.4074074074),(10,157.1428571429),(20,123.3333333333),(50,136),(100,79.2079207921),(200,63.2),(500,46.5608465608),(1000,24.8031496063),(2000,24.0625),(5000,4)]
								

ohsumed_ml = [(5,0),(10,0.-50),(20,100),(50,50),(100,95.1219512195),(200,95),(500,38.3720930233),(1000,18.4426229508),(2000,6.1224489796),(5000,3.3018867925)]

				


print ''
print ''


plt.clf

p_uvigomed_sl, = plt.plot(train_set,  [x[1] for x in uvigomed_sl],'ko-')

plt.xlabel('Training sequence')
plt.ylabel('% improvement')
plt.legend([p_uvigomed_sl], ["UVigoMED_SL"], loc = "lower right", prop={'size':12})
plt.savefig("Results/json/uvigomed_sl")

plt.clf()

p_uvigomed_ml, = plt.plot(train_set,  [x[1] for x in uvigomed_ml],'ko-')

plt.xlabel('Training sequence')
plt.ylabel('% improvement')
plt.legend([p_uvigomed_ml], ["UVigoMED_ML"], loc = "lower right", prop={'size':12})
plt.savefig("Results/json/uvigomed_ml")


plt.clf()

p_ohsumed_sl, = plt.plot(train_set,  [x[1] for x in ohsumed_sl],'ko-')

plt.xlabel('Training sequence')
plt.ylabel('% improvement')
plt.legend([p_ohsumed_sl], ["OHSUMED_SL"], loc = "lower right", prop={'size':12})
plt.savefig("Results/json/ohsumed_sl")

plt.clf()

p_ohsumed_ml, = plt.plot(train_set,  [x[1] for x in ohsumed_ml],'ko-')

plt.xlabel('Training sequence')
plt.ylabel('% improvement')
plt.legend([p_ohsumed_ml], ["OHSUMED_ML"], loc = "lower right", prop={'size':12})
plt.savefig("Results/json/ohsumed_ml")



#plt.savefig("Results/json/Multilabel/" + experiment_folder + "/" + experiment_folder.replace(".","_"))
