import util_classify
import classify_methods

from sklearn.metrics import classification_report, f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import hamming_loss

import sys
import argparse
import json
import time
import os

class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open("Results/" + filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def close(self):
        self.log.close()

# Parameters available to iterate
corpora_available = ["boc_reuters_27000","bow_reuters_27000","boc_ohsumed","bow_ohsumed","boc_ohsumed_expanded","boc_20_newsgroup","bow_20_newsgroup","boc_ieee","bow_ieee","boc_ieee_expanded",
"boc_20_newsgroup_expanded","boc_reuters_21578","bow_reuters_21578","boc_reuters_21578_expanded", "bow_oercommons", "boc_oercommons","bow_merlot","bow_ohsumed_multilabel","boc_ohsumed_multilabel",
"bow_uvigomed_multilabel","boc_uvigomed_multilabel","bow_uvigomed","boc_uvigomed", "bow_ohsumed_randomized","boc_ohsumed_randomized","boc_ohsumed_randomized_multilabel",
"bow_ohsumed_randomized_multilabel","bow_reuters_rcv1", "bow_reuters_rcv2","boc_reuters_rcv1", "boc_reuters_rcv2","bow_reuters_rcv2_translated_to_english_google_translate",
"boc_wikipedia_english","boc_wikipedia_spanish", "bow_wikipedia_english", "bow_wikipedia_spanish", "bow_wikipedia_spanish_translated_to_english_google_translate"]
classify_methods_available = ["mbayes", "kneighbors","multilabel","SVM","linear_SVM","nu_SVM"]
threshold_available = [0.01, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
weighting_available = ["milne", "binary"] #centrodid
metrics_available = ["cosine","jaccard","braycurtis","mahalanobis"]
kernel_functions_available = ["linear","poly","rbf","sigmoid"]

parser = argparse.ArgumentParser(description = 'Classifier')
parser.add_argument('-corpus', dest='corpus', default="all", help="If empty, use all available corpora.", choices=['boc_reuters_27000','bow_reuters_27000','boc_ohsumed','bow_ohsumed','boc_ohsumed_expanded','boc_20_newsgroup','bow_20_newsgroup','boc_ieee','bow_ieee','boc_ieee_expanded','boc_20_newsgroup_expanded','boc_reuters_21578','bow_reuters_21578','boc_reuters_21578_expanded','bow_oercommons', 'boc_oercommons','bow_merlot','bow_ohsumed_multilabel','boc_ohsumed_multilabel','bow_uvigomed_multilabel','boc_uvigomed_multilabel','bow_uvigomed','boc_uvigomed','bow_ohsumed_randomized','boc_ohsumed_randomized','boc_ohsumed_randomized_multilabel','bow_ohsumed_randomized_multilabel','bow_reuters_rcv1', 'bow_reuters_rcv2','boc_reuters_rcv1', 'boc_reuters_rcv2','bow_reuters_rcv2_translated_to_english_google_translate'])
parser.add_argument('-corpus_training', dest='corpus_training', default = "none", choices=['bow_reuters_rcv1', 'bow_reuters_rcv2','boc_reuters_rcv1', 'boc_reuters_rcv2','boc_wikipedia_english', 'bow_wikipedia_english'])
parser.add_argument('-corpus_test', dest='corpus_test', default="none", choices=['bow_reuters_rcv1', 'bow_reuters_rcv2','boc_reuters_rcv1', 'boc_reuters_rcv2', 'bow_reuters_rcv2_translated_to_english_google_translate', 'boc_wikipedia_spanish', 'bow_wikipedia_english', 'boc_wikipedia_english', 'bow_wikipedia_spanish_translated_to_english_google_translate'])
parser.add_argument('-method', dest='classify_method', default = "mbayes", help="Classification method, default mbayes.", choices =  ["all", "mbayes", "kneighbors","multilabel","SVM","linear_SVM", "nu_SVM","cross_language_linear_SVM"])
parser.add_argument('-threshold', dest='threshold', default = 0.01, type = float, help = "Annotations threshold. Default 0.01", choices =  threshold_available)
parser.add_argument('-test', dest='test', default = 0, type = int, help = "Test number documents. If empty, all.")
parser.add_argument('-train', dest='train', default = 0, type = int ,help = "Training number documents. If empty, all.")
parser.add_argument('-weighting',  dest='weighting', default = "milne", help = "Weighting used. Default Milne weighting.", choices =  ['all', 'milne', 'centroid', 'binary'])
parser.add_argument('-smoothing',  dest='smoothing', default = 0.001, type = float,  help = "mbayes Smoothing. Alpha param in MultinomialMB class.")
parser.add_argument('-exp_threshold',  dest='expansion_threshold', default = 1, type = float,  help = "")
parser.add_argument('-exp_relatedness',  dest='expansion_relatedness', default = 1, type = float,  help = "")
parser.add_argument('-exp_weighting', dest='expanded_weighting', default = 0.1, type = float, help = "")
parser.add_argument('-kbest', dest='kbest', default = 3000, type = int, help = "")
parser.add_argument('-n_neighbors', dest="n_neighbors", default = 10, type=int, help="")
parser.add_argument('-metric', dest="metric", default = "cosine", help="", choices = ['cosine', 'jaccard', 'braycurtis', 'mahalanobis', 'euclidean', 'manhattan', 'chebyshev', 'seuclidean'])
parser.add_argument('-destination_folder', dest="destination_folder", help="Destination folder to store .json experiment results file.")
parser.add_argument('-algorithm', dest="algorithm", default = "SVC", help="Multilabel algorithm to use.", choices = ['SVC','Bayes','KNN','SGD', 'SVC_rbf','SVC_poly','SVC_sigmoid','linear_SVC'])
parser.add_argument('-kernel', dest="kernel", default = "linear", help="Kernel function to SVM classifier.", choices = ['linear','poly','rbf','sigmoid'])
parser.add_argument('-nu', dest='nu', default = 0.5, type = float, help = "Nu param to NuSVM algorithm.")
parser.add_argument('-metadata_freq', dest="metadata_freq", default = 0, type=int, help="")

args = parser.parse_args()

# INPUT PARAMETERS
if args.corpus_training == "none" and args.corpus_test == "none":
    if args.corpus == 'all':
        array_corpus = corpora_available
    else:
        array_corpus = [args.corpus]
else:
    array_corpus = ["cross_language"]  # is not a corpus, it is only to indicate that will make use of a corpus to train and another for test

if args.classify_method == 'all':
    array_classify_methods = classify_methods_available
else:
    array_classify_methods = [args.classify_method]

array_threshold = [args.threshold]

if args.weighting == 'all':
    array_weighting = weighting_available
else:
    array_weighting = [args.weighting]

smoothing = args.smoothing
expansion_threshold = args.expansion_threshold
expansion_relatedness = args.expansion_relatedness
expanded_weighting = args.expanded_weighting
kbest = args.kbest
n_neighbors = args.n_neighbors
metric = args.metric
destination_folder = args.destination_folder
algorithm = args.algorithm
kernel = args.kernel
nu = args.nu
corpus_training = args.corpus_training
corpus_test = args.corpus_test
classify_method = array_classify_methods[0]
tfidf = False           # not operative yet
stemming = "porter"     # not operative yet
weighting = array_weighting[0]
metadata_freq = args.metadata_freq

if metadata_freq > 0:
    metadata = "yes"
else:
    metadata = "no"
    metadata_freq = 0

if args.classify_method == "mbayes":
    json_path = "Results/json/BAYES/" + destination_folder + "/"
elif args.classify_method == "kneighbors":
    json_path = "Results/json/KNN/" + destination_folder + "/"
elif args.classify_method == "multilabel":
    json_path = "Results/json/Multilabel/" + destination_folder + "/"
elif args.classify_method == "SVM" or args.classify_method == "linear_SVM" or args.classify_method == "nu_SVM":
    json_path = "Results/json/SVM/" + destination_folder + "/"
elif args.classify_method == "cross_language_linear_SVM":
    json_path = "Results/json/cross_language_SVM/" + destination_folder + "/"

if os.path.exists(json_path) == False:
    os.mkdir(json_path)
# END INPUT PARAMETERS

# MAIN
for corpus in array_corpus:

    if args.train == 0 and args.test == 0:
        if 'reuters' in corpus:
            array_number_of_documents_for_training = [2400]
            array_number_of_documents_for_testing = [500]
        elif 'ieee' in corpus:
            array_number_of_documents_for_training = [550]
            array_number_of_documents_for_testing = [140]
        else:
            array_number_of_documents_for_training = [args.train]
            array_number_of_documents_for_testing = [args.test]

    else:
        array_number_of_documents_for_training = [args.train]
        array_number_of_documents_for_testing = [args.test]

    number_of_documents_for_testing = array_number_of_documents_for_testing[0]

    for number_of_documents_for_training in array_number_of_documents_for_training:
        for threshold in array_threshold:

            # Create file where the results of the experiment will be saved and we make stdout go to screen and files
            if number_of_documents_for_training == 0 and number_of_documents_for_testing == 0:
                filename = corpus + "_th_" + (str(threshold)).replace("0.", "") + "_all_" + classify_method + ".txt"
            else:
                filename = corpus + "_th_" + (str(threshold)).replace("0.", "") + "_" + str(number_of_documents_for_training) + "_" + str(number_of_documents_for_testing) + "_" + classify_method + ".txt"

            old_stdout = sys.stdout
            sys.stdout = Logger(filename)

            # Print experiment details
            util_classify.print_experiment_details(corpus, corpus_training, corpus_test, threshold, number_of_documents_for_training, number_of_documents_for_testing, classify_method, tfidf, stemming, smoothing, weighting, expansion_threshold, expansion_relatedness, expanded_weighting, n_neighbors, metric, algorithm, kernel, nu)

            # Establish session with the database
            if corpus != 'cross_language':
                util_classify.set_database_session(corpus)
            else:
                util_classify.set_database_session(corpus_training)

            # Get training and test documents separately and the lists of unique words with their frequency
            print "Getting train and test documents..."
            if args.classify_method == "multilabel":
                if "boc" in corpus:
                    documents_training, documents_test = util_classify.get_documents_from_multilabel_database_boc(corpus, threshold, weighting, expansion_threshold, expansion_relatedness, number_of_documents_for_training, expanded_weighting, number_of_documents_for_testing)
                    words_features = util_classify.get_unique_words_boc(documents_training)
                elif "bow" in corpus:
                    documents_training, documents_test = util_classify.get_documents_from_multilabel_database_bow(corpus, number_of_documents_for_training, metadata, metadata_freq, number_of_documents_for_testing)
                    words_features = util_classify.get_unique_words_bow(documents_training)
            elif args.classify_method == "cross_language_linear_SVM":
                if "boc" in corpus_training and "boc" in corpus_test:
                    documents_training, documents_test = util_classify.get_documents_from_cross_language_database_boc(corpus_training, corpus_test, threshold, weighting, expansion_threshold, expansion_relatedness, number_of_documents_for_training, expanded_weighting, number_of_documents_for_testing)
                    words_features = util_classify.get_unique_words_boc(documents_training)
                elif "bow" in corpus_training and "bow" in corpus_test:
                    documents_training, documents_test = util_classify.get_documents_from_cross_language_database_bow(corpus_training, corpus_test, threshold, weighting, expansion_threshold, expansion_relatedness, number_of_documents_for_training, expanded_weighting, number_of_documents_for_testing)
                    words_features = util_classify.get_unique_words_bow(documents_training)
            else:
                if "boc" in corpus:
                    documents_training, documents_test = util_classify.get_documents_from_database_boc(corpus, threshold, weighting, expansion_threshold, expansion_relatedness, number_of_documents_for_training, expanded_weighting, number_of_documents_for_testing)
                    words_features = util_classify.get_unique_words_boc(documents_training)
                elif "bow" in corpus:
                    documents_training, documents_test = util_classify.get_documents_from_database_bow(corpus, number_of_documents_for_training, number_of_documents_for_testing)
                    words_features = util_classify.get_unique_words_bow(documents_training)

            # Classify and print classification report
            # K-neighbours
            if classify_method == "all_classifiers" or classify_method == "kneighbors":
                original_categories, estimated_categories = classify_methods.kneighbors(corpus, documents_training, documents_test, words_features, n_neighbors, metric, kbest)
                print classification_report(original_categories, estimated_categories, target_names = util_classify.get_categories(corpus))
                f1_score_result = f1_score(original_categories, estimated_categories, pos_label=None, average = 'macro')

            # Multinomial bayes
            if classify_method == "all_classifiers" or classify_method == "mbayes":
                if tfidf == True:
                    original_categories, estimated_categories = classify_methods.multinomial_bayes_nltk_wrapper(corpus, documents_training, documents_test, words_features, smoothing, kbest)
                else:
                    original_categories, estimated_categories = classify_methods.multinomial_bayes_sklearn(corpus, documents_training, documents_test, words_features, smoothing)
                print classification_report(original_categories,estimated_categories,target_names=util_classify.get_categories(corpus))
                f1_score_result = f1_score(original_categories,estimated_categories, pos_label=None, average = 'macro')

            # Support Vector Machines
            if classify_method == "all_classifiers" or classify_method == "SVM":
                original_categories, estimated_categories = classify_methods.support_vector_machines(corpus, documents_training, documents_test, words_features, kernel)
                print classification_report(original_categories,estimated_categories,target_names=util_classify.get_categories(corpus))
                f1_score_result = f1_score(original_categories,estimated_categories, pos_label=None, average = 'macro')

            # Linear Support Vector Machines
            if classify_method == "all_classifiers" or classify_method == "linear_SVM":
                if tfidf == True:
                    original_categories, estimated_categories = classify_methods.linear_support_vector_machines_tf_idf(corpus, documents_training, documents_test, words_features, kbest)
                else:
                    original_categories, estimated_categories = classify_methods.linear_support_vector_machines(corpus, documents_training, documents_test, words_features)
                print classification_report(original_categories,estimated_categories,target_names=util_classify.get_categories(corpus))
                f1_score_result = f1_score(original_categories,estimated_categories, pos_label=None, average = 'macro')
                precision = precision_score(original_categories,estimated_categories)
                recall = recall_score(original_categories,estimated_categories)

            # Cross-Language Support Vector Machines
            if classify_method == "cross_language_linear_SVM":
                original_categories, estimated_categories = classify_methods.linear_support_vector_machines_cross_language(corpus_training, corpus_test, documents_training, documents_test, words_features)
                print classification_report(original_categories,estimated_categories,target_names=util_classify.get_categories(corpus_test))
                f1_score_result = f1_score(original_categories,estimated_categories, pos_label= None, average = 'macro')
                precision = precision_score(original_categories,estimated_categories)
                recall = recall_score(original_categories,estimated_categories)

            # nu-Support Vector Machines
            if classify_method == "all_classifiers" or classify_method == "nu_SVM":
                original_categories, estimated_categories = classify_methods.nu_support_vector_machines(corpus, documents_training, documents_test, words_features, kernel, nu)
                print classification_report(original_categories,estimated_categories,target_names=util_classify.get_categories(corpus))
                f1_score_result = f1_score(original_categories,estimated_categories, pos_label= None, average = 'macro')

            #Multilabel
            if classify_method == "all_classifiers" or classify_method == "multilabel":
                ground_truth_vector_categories, prediction = classify_methods.multilabel(corpus, documents_training, documents_test, words_features, smoothing, algorithm)
                print "Metrics:"
                print "----------------"
                print "Hamming Loss:"
                hamming_loss = hamming_loss(ground_truth_vector_categories, prediction)
                print hamming_loss
                print
                print "Accuracy:"
                accuracy = accuracy_score(ground_truth_vector_categories, prediction)
                print accuracy
                print
                print "Precision:"
                precision = precision_score(ground_truth_vector_categories, prediction)
                print precision
                print
                print "Recall:"
                recall = recall_score(ground_truth_vector_categories, prediction)
                print recall
                print
                print "Classification Report:"
                print classification_report(ground_truth_vector_categories, prediction, target_names=util_classify.get_multiple_categories(corpus))
                print "F1-score"
                f1_score_result = f1_score(ground_truth_vector_categories, prediction, pos_label= None, average = 'macro')
                print "----------------"

            print "F1_SCORE (Macro): " +str(f1_score_result)
            print "Precision: " + str(precision)
            print "Recall: " + str(recall)

            if classify_method == "multilabel":
                filename = corpus + "_th_"+ (str(threshold)).replace("0.","") + "_" + str(number_of_documents_for_training) + "_" + str(number_of_documents_for_testing) + "_" + classify_method + "_" + str(n_neighbors) + "_neighbors" +str(int(time.time()))+  ".json"
                with open(json_path + filename, "w") as outfile:
                    json.dump(util_classify.get_experiment_multilabel_results(corpus, threshold,number_of_documents_for_training, number_of_documents_for_testing, classify_method,tfidf,stemming,smoothing, weighting, expansion_threshold, expansion_relatedness, f1_score_result, expanded_weighting, kbest, n_neighbors, metric, hamming_loss, accuracy, precision, recall, algorithm, metadata_freq), outfile)
            elif "cross_language" in classify_method:
                filename = corpus_training + "_" + corpus_test + "_th_"+ (str(threshold)).replace("0.","") + "_" + str(number_of_documents_for_training) + "_" + str(number_of_documents_for_testing) + "_" + classify_method + "_" + str(n_neighbors) + "_neighbors" +str(int(time.time()))+  ".json"
                with open(json_path + filename, "w") as outfile:
                    json.dump(util_classify.get_experiment_cross_language_results(corpus, corpus_training, corpus_test, threshold,number_of_documents_for_training, number_of_documents_for_testing, classify_method,tfidf,stemming,smoothing, weighting, expansion_threshold, expansion_relatedness, f1_score_result, expanded_weighting, kbest, n_neighbors, metric, kernel, nu, precision, recall), outfile)
            else:
                filename = corpus + "_th_"+ (str(threshold)).replace("0.","") + "_" + str(number_of_documents_for_training) + "_" + str(number_of_documents_for_testing) + "_" + classify_method + "_" + str(n_neighbors) + "_neighbors" +str(int(time.time()))+  ".json"
                with open(json_path + filename, "w") as outfile:
                    json.dump(util_classify.get_experiment_results(corpus, threshold, number_of_documents_for_training, number_of_documents_for_testing, classify_method, tfidf, stemming, smoothing, weighting, expansion_threshold, expansion_relatedness, f1_score_result, expanded_weighting, kbest, n_neighbors, metric, kernel, nu, precision, recall), outfile)

            print "---- Execution End ----"
            sys.stdout.close()
            sys.stdout = old_stdout