from sklearn.neighbors import KNeighborsClassifier
from sqlalchemy.orm import sessionmaker
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
import numpy as np
from sklearn import linear_model
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import ExtraTreesClassifier
#import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestClassifier

import util_classify
import time
from db_simplified_declarative import Document


WordFeatures = None
DBSession = sessionmaker()
Session = DBSession()


def kneighbors(corpus, documents_training, documents_test, words_features, n_neighbors, metric, kbest):
    """
    KNeighbors Algorithm
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param n_neighbors:
    :param metric:
    :param kbest:
    :return:
    """

    print
    print "----- KNeighbors Algorithm ------"
    print "Creating Training Vectors..."
    array_vector_training = []
    array_categories = []
    for (id, original_category, annotations) in documents_training:
        array_vector_training.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        array_categories.append(util_classify.get_categories(corpus).index(original_category))    
        
    print "Training the algorithm..."
    X = array_vector_training
    y = array_categories

    if kbest == 0:
        kbest = "all"

    if kbest == "all":
        if metric == "cosine":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.cosine_measure)
        elif metric == "jaccard":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.jaccard_measure)
        elif metric == "braycurtis":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.braycurtis_measure)
        elif metric == "mahalanobis":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.mahalanobis_measure)
        elif metric == "euclidean":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.euclidean_measure)
        elif metric == "manhattan":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.manhattan_measure)
        elif metric == "chebyshev":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.chebyshev_measure)
        elif metric == "seuclidean":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.seuclidean_measure)
        neigh.fit(X, y)
    elif kbest != "all":
        print ("Extracting %d best features by a chi-squeared test" %kbest)
        ch2 = SelectKBest(chi2, k=kbest)
        X = ch2.fit_transform(X,y)
        print "Done!"
        if metric == "cosine":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.cosine_measure)
        elif metric == "jaccard":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.jaccard_measure)
        elif metric == "braycurtis":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.braycurtis_measure)
        elif metric == "mahalanobis":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.mahalanobis_measure)
        elif metric == "euclidean":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.euclidean_measure)
        elif metric == "manhattan":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.manhattan_measure)
        elif metric == "chebyshev":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.chebyshev_measure)
        elif metric == "seuclidean":
            neigh = KNeighborsClassifier(n_neighbors=n_neighbors, metric='pyfunc', func=util_classify.seuclidean_measure)
        neigh.fit(X, y)

    print "Calculating metrics..."

    estimated_categories = []
    original_categories = []

    for (id ,original_category, annotations) in documents_test: 
        vector = util_classify.transform_document_in_vector(annotations, words_features, corpus)
        if kbest != "all":
            vector = ch2.transform(vector)
        cat_classify = neigh.predict(vector)
        estimated_categories.append(util_classify.get_categories(corpus)[cat_classify])
        original_categories.append(original_category)
    return original_categories, estimated_categories


def multinomial_bayes_nltk_wrapper(corpus, documents_training, documents_test, words_features, smoothing, kbest):
    """
    Multinomial Naive Bayes Algorithm using wrapper NLTK SklearnClassifier
    Memory problems can occur if very large dataset
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param smoothing:
    :param kbest:
    :return:
    """

    print
    print "----- Multinomial Bayes with wrapper nltk Algorithm------"
    print "Creating Training Feature Vectors..."
    array_features_training = []
    for (id, original_category, annotations) in documents_training:
        array_features_training.append((util_classify.transform_document_in_dict(annotations, words_features, corpus), original_category))
    # array_features_training = apply_features(extract_document_features,documents_training)
    print "Training algorithm..."
    # ('chi2', SelectKBest(chi2, k=3000)),
    if kbest == 0:
        kbest = "all"
    pipeline = Pipeline([('chi2', SelectKBest(chi2, k=kbest)), ('tfidf', TfidfTransformer()),
                         ('nb', MultinomialNB(alpha=smoothing))])

    # pipeline = Pipeline([('nb', MultinomialNB(alpha=smoothing))])

    classifier = SklearnClassifier(pipeline)
    classifier.train(array_features_training)

    print "Calculating metrics ..."
    categories = util_classify.get_categories(corpus)
    estimated_categories = []
    original_categories = []               

    for (id, cat_original, annotations) in documents_test:
        cat_estimated = classifier.classify((util_classify.transform_document_in_dict(annotations, words_features, corpus)))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))
    return original_categories, estimated_categories


def multinomial_bayes_sklearn(corpus, documents_training, documents_test, words_features, smoothing):
    """
    Multinomial Naive Bayes sing only MultinomialNB sklearn library
    Training in parts to avoid memory problems
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param smoothing:
    :return:
    """

    print "-----Multinomial Bayes sklearn pure algorithm------"
    categories = util_classify.get_categories(corpus)    
    classifier = MultinomialNB(alpha=smoothing)
          
    '''
    print "Entrenando algoritmo por completo..."
    X_train_features = []
    y_train_categories = []
    ##### Entrenandolo de golpe
    for (id ,original_category, annotations) in documents_training:        
        X_train_features.append(util_classify.transform_document_in_vector(annotations,words_features,corpus)) 
        y_train_categories.append(original_category)
    
    classifier.fit(np.array(X_train_features), np.array(y_train_categories))    
    '''
    
    # Training in parts
    print "Training algorithm in parts..."
    first = True
    for (id, original_category, annotations) in documents_training:
        if first is True:
            classifier.partial_fit(np.array(util_classify.transform_document_in_vector(annotations, words_features, corpus)), np.array([original_category]), classes=categories)
            first = False
        else:
            classifier.partial_fit(np.array(util_classify.transform_document_in_vector(annotations, words_features, corpus)), np.array([original_category]))
                      
    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []               
    
    for (id, cat_original, annotations) in documents_test:
        cat_estimated = classifier.predict(np.array((util_classify.transform_document_in_vector(annotations, words_features, corpus))))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))
    return original_categories, estimated_categories


def multilabel(corpus, documents_training, documents_test, words_features, smoothing, algorithm):
    """
    Multilabel algorithm
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param smoothing:
    :param algorithm:
    :return:
    """

    print "----- Multilabel Algorithm------"
    print "Creating Training Vectors..."
    print "Creating Training Feature Vectors..."

    print corpus

    util_classify.set_database_session(corpus)


    ids_documents_test = []

    first_time = 0
    first_time_categories = 0
    for (id, original_category, annotations) in documents_training:
        vector = util_classify.transform_document_in_vector(annotations, words_features, corpus)
        vector = np.array(vector)
        if first_time == 0:
            array_vector_training = vector
            first_time = 1
        else:
            array_vector_training = np.vstack((array_vector_training, vector))

        original_categories = [x.strip() for x in original_category.split(',')]

        # OERCOMMONS corpus -> 21 categories
        # MERLOT corpus -> 9 categories
        # OHSUMED corpus -> 23 categories
        # CNX corpus -> 6 categories
        # Common categories -> 6 categories
        vector_categories = np.zeros(21)
        for category in original_categories:
            vector_categories[util_classify.get_multiple_categories(corpus).index(category)] = 1
        vector_categories = np.array(vector_categories)
        if first_time_categories == 0:
            array_vector_categories = vector_categories
            first_time_categories = 1
        else:
            array_vector_categories = np.vstack((array_vector_categories, vector_categories))


    print "Training multilabel classifier..."
    if algorithm == "SVC":
        classifier = OneVsRestClassifier(SVC(kernel='linear'))
    elif algorithm == "SVC_rbf":
        classifier = OneVsRestClassifier(SVC(kernel='rbf', gamma=10.0))
    elif algorithm == "SVC_poly":
        classifier = OneVsRestClassifier(SVC(kernel='poly'))
    elif algorithm == "SVC_sigmoid":
        classifier = OneVsRestClassifier(SVC(kernel='sigmoid'))
    elif algorithm == "linear_SVC":
        classifier = OneVsRestClassifier(LinearSVC())
    elif algorithm == "Bayes":
        classifier = OneVsRestClassifier(MultinomialNB())
    elif algorithm == "KNN":
        classifier = OneVsRestClassifier(KNeighborsClassifier())
    elif algorithm == "SGD":
        classifier = OneVsRestClassifier(linear_model.SGDClassifier())

    classifier.fit(array_vector_training, array_vector_categories)

    print "Classifying test documents (Prediction)"
    first_time = 0
    first_time_categories = 0
    for (id, original_category, annotations) in documents_test:
        ids_documents_test.append(id)
        vector = util_classify.transform_document_in_vector(annotations, words_features, corpus)
        vector = np.array(vector)
        if first_time == 0:
            array_vector_test = vector
            first_time = 1
        else:
            array_vector_test = np.vstack((array_vector_test, vector))

        # From here we calculate the vector of original categories for test documents to be used as ground truth when making measurements
        original_categories = [x.strip() for x in original_category.split(',')]
        # OERCOMMONS corpus -> 21 categories
        # MERLOT corpus -> 9 categories
        # OHSUMED corpus -> 23 categories
        # CNX corpus -> 6 categories
        # Common categories -> 6 categories

        vector_categories = np.zeros(21)
        for category in original_categories:
            vector_categories[util_classify.get_multiple_categories(corpus).index(category)] = 1
        vector_categories = np.array(vector_categories)
        if first_time_categories == 0:
            ground_truth_vector_categories = vector_categories
            first_time_categories = 1
        else:
            ground_truth_vector_categories = np.vstack((ground_truth_vector_categories, vector_categories))


    prediction = classifier.predict(array_vector_test)

    # Storage process predicted categories in DB
    '''
    for document in Session.query(Document):
        if document.id in ids_documents_test:
            categories_list = ""
            pos = ids_documents_test.index(document.id)
            document_prediction = prediction[pos]
            matches = [item for item in range(len(document_prediction)) if document_prediction[item] == 1]
            for i in matches:
                category = util_classify.get_multiple_categories(corpus)[i]
                categories_list = categories_list + category + ","
            categories_list = categories_list[:-1]
            document.classified_in_category = categories_list

            if "oercommons" in corpus:
                document.classified_in_category_oercommons = categories_list
            elif "merlot" in corpus:
                document.classified_in_category_merlot = categories_list
            elif "cnx" in corpus:
                document.classified_in_category_cnx = categories_list
            elif "wikipedia" in corpus:
                document.classified_in_category_wikipedia = categories_list

    Session.commit()
    # End storage process predicted categories in DB
    '''
    return ground_truth_vector_categories, prediction


def multilabel_feature_selection(corpus, documents_training, documents_test, words_features, smoothing, algorithm):
    """
    Multilabel algorithm
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param smoothing:
    :param algorithm:
    :return:
    """

    print "----- Multilabel Algorithm------"
    print "Creating Training Vectors..."
    print "Creating Training Feature Vectors..."

    print corpus

    util_classify.set_database_session(corpus)


    print type(words_features)
    print words_features
    print len(words_features)

    ids_documents_test = []
    array_features = []

    first_time = 0
    first_time_categories = 0
    for (id, original_category, annotations) in documents_training:
        print annotations
        print type(annotations[0])
        print type(annotations)
        vector = util_classify.transform_document_in_vector(annotations, words_features, corpus)
        vector = np.array(vector)
        if first_time == 0:
            array_vector_training = vector
            first_time = 1
        else:
            array_vector_training = np.vstack((array_vector_training, vector))

        original_categories = [x.strip() for x in original_category.split(',')]


        # OERCOMMONS corpus -> 21 categories
        # MERLOT corpus -> 9 categories
        # OHSUMED corpus -> 23 categories
        # CNX corpus -> 6 categories
        # Common categories -> 6 categories
        vector_categories = np.zeros(21)
        for category in original_categories:
            vector_categories[util_classify.get_multiple_categories(corpus).index(category)] = 1
        vector_categories = np.array(vector_categories)
        if first_time_categories == 0:
            array_vector_categories = vector_categories
            first_time_categories = 1
        else:
            array_vector_categories = np.vstack((array_vector_categories, vector_categories))

    '''
    #Load boston housing dataset as an example
    boston = load_boston()
    names = boston["feature_names"]
    print type(names)
    rf = RandomForestRegressor()
    rf.fit(array_vector_training, array_vector_categories)
    print "Features sorted by their score:"
    print sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names),
                 reverse=True)
    '''



    '''
    # Build a forest and compute the feature importances
    forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

    forest.fit(array_vector_training, array_vector_categories)

    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
    print std
    indices = np.argsort(importances)[::-1]

    print "words features"
    print words_features
    print len(words_features)
    print type(words_features)


    for key, value in words_features.iteritems():
        array_features.append(key)
    print "Array Features"
    print array_features

    print "Indices"
    print indices


    # Print the feature ranking
    print("Feature ranking:")

    outfile = open('features_2000_test_used_to_train_bueno.txt', 'w') # Indicamos el valor 'w'.
    for f in range(500000):
        print("%d. feature %d (%f) : %s" % (f + 1, indices[f], importances[indices[f]], array_features[indices[f]].encode('utf-8')))
        outfile.write("%d. feature %d (%f) : %s \n" % (f + 1, indices[f], importances[indices[f]], array_features[indices[f]].encode('utf-8')))


    outfile.close()


    print "a"
    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(10), importances[indices],
           color="r", yerr=std[indices], align="center")
    plt.xticks(range(10), indices)
    plt.xlim([-1, 10])
    plt.show()

    '''

    #Random Forest Classifier

    print "array vector training"
    print array_vector_training
    print

    print "array vector training shape"
    print array_vector_training.shape

    print
    print "array_vector_training type"
    print type(array_vector_training)


    for key, value in words_features.iteritems():
        array_features.append(key)
    print "Array Features"
    print array_features



    forest = RandomForestClassifier(n_estimators=10000,
                               random_state=0,
                                n_jobs=-1)

    forest.fit(array_vector_training, array_vector_categories)
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]

    outfile = open('borrar.txt', 'w') # Indicamos el valor 'w'.

    for f in range(array_vector_training.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30,  array_features[indices[f]].encode('utf-8'), importances[indices[f]]))
        outfile.write("%2d) %-*s %f \n" % (f + 1, 30,  array_features[indices[f]].encode('utf-8'), importances[indices[f]]))


    print array_vector_training.shape
    print array_vector_categories.shape

    print "sleeping"

    time.sleep(1000)

    print "Training multilabel classifier with feature selection first..."

    clf = Pipeline([
        ('feature_selection', RandomForestClassifier(n_estimators=10000,random_state=0,n_jobs=-1)),
        ('classification', LinearSVC())
        ])

    multiclf = OneVsRestClassifier(clf)

    multiclf.fit(array_vector_training, array_vector_categories)

    #classifier = OneVsRestClassifier(LinearSVC())

    #classifier.fit(array_vector_training, array_vector_categories)

    print "Classifying test documents (Prediction)"
    first_time = 0
    first_time_categories = 0
    for (id, original_category, annotations) in documents_test:
        ids_documents_test.append(id)
        vector = util_classify.transform_document_in_vector(annotations, words_features, corpus)
        vector = np.array(vector)
        if first_time == 0:
            array_vector_test = vector
            first_time = 1
        else:
            array_vector_test = np.vstack((array_vector_test, vector))

        # From here we calculate the vector of original categories for test documents to be used as ground truth when making measurements
        original_categories = [x.strip() for x in original_category.split(',')]
        # OERCOMMONS corpus -> 21 categories
        # MERLOT corpus -> 9 categories
        # OHSUMED corpus -> 23 categories
        # CNX corpus -> 6 categories
        # Common categories -> 6 categories

        vector_categories = np.zeros(21)
        for category in original_categories:
            vector_categories[util_classify.get_multiple_categories(corpus).index(category)] = 1
        vector_categories = np.array(vector_categories)
        if first_time_categories == 0:
            ground_truth_vector_categories = vector_categories
            first_time_categories = 1
        else:
            ground_truth_vector_categories = np.vstack((ground_truth_vector_categories, vector_categories))


    prediction = multiclf.predict(array_vector_test)

    # Storage process predicted categories in DB
    '''
    for document in Session.query(Document):
        if document.id in ids_documents_test:
            categories_list = ""
            pos = ids_documents_test.index(document.id)
            document_prediction = prediction[pos]
            matches = [item for item in range(len(document_prediction)) if document_prediction[item] == 1]
            for i in matches:
                category = util_classify.get_multiple_categories(corpus)[i]
                categories_list = categories_list + category + ","
            categories_list = categories_list[:-1]
            document.classified_in_category = categories_list

            if "oercommons" in corpus:
                document.classified_in_category_oercommons = categories_list
            elif "merlot" in corpus:
                document.classified_in_category_merlot = categories_list
            elif "cnx" in corpus:
                document.classified_in_category_cnx = categories_list
            elif "wikipedia" in corpus:
                document.classified_in_category_wikipedia = categories_list

    Session.commit()
    # End storage process predicted categories in DB
    '''
    return ground_truth_vector_categories, prediction


def support_vector_machines(corpus, documents_training, documents_test, words_features, kernel):
    """
    Support Vector Machines Algorithm
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param kernel:
    :return:
    """

    print
    print "----- Support Vector Machines Algorithm------"
    print "Creating Training Vectors..."
    categories = util_classify.get_categories(corpus)  

    array_vector_training = []
    array_categories = []
    for (id, original_category, annotations) in documents_training:
        array_vector_training.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        array_categories.append(util_classify.get_categories(corpus).index(original_category))    
        
    print "Training the algorithm..."
    classifier = SVC(kernel=kernel)    

    X_train_features = []
    y_train_categories = []
    # Train all
    for (id, original_category, annotations) in documents_training:
        X_train_features.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        y_train_categories.append(original_category)

    classifier.fit(np.array(X_train_features), np.array(y_train_categories))    

    print "Calculating metrics ..."
    estimated_categories = []
    original_categories = []

    for (id, cat_original, annotations) in documents_test:
        cat_estimated = classifier.predict(np.array((util_classify.transform_document_in_vector(annotations, words_features, corpus))))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))
    return original_categories, estimated_categories


def linear_support_vector_machines(corpus, documents_training, documents_test, words_features):
    """
    Linear Support Vector Machines Algorithm. The Support Vector Machines algorithm with a linear kernel
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :return:
    """

    print
    print "----- Linear Support Vector Machines Algorithm------"
    print "Creating Training Vectors..."
    categories = util_classify.get_categories(corpus)
    array_vector_training = []
    array_categories = []

    for (id, original_category, annotations) in documents_training:
        array_vector_training.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        array_categories.append(util_classify.get_categories(corpus).index(original_category))    
        
    print "Training the algorithm..."
    classifier = LinearSVC()

    X_train_features = []
    y_train_categories = []
    # Train all
    for (id, original_category, annotations) in documents_training:
        X_train_features.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        y_train_categories.append(original_category)

    classifier.fit(np.array(X_train_features), np.array(y_train_categories))    

    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []

    for (id ,cat_original, annotations) in documents_test:
        cat_estimated = classifier.predict(np.array((util_classify.transform_document_in_vector(annotations, words_features, corpus))))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))
    return original_categories, estimated_categories


def linear_support_vector_machines_tf_idf(corpus, documents_training, documents_test, words_features, kbest):
    """
    Linear Support Vector Machines Algorithm. The Support Vector Machines algorithm with a linear kernel and using TF/IDF
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param kbest:
    :return:
    """

    print
    print "----- Linear Support Vector Machines with tfidf algorithm ------"
    print "Creating Features Training Vectors..."
    categories = util_classify.get_categories(corpus)
    array_features_training = []

    for (id, original_category, annotations) in documents_training:
        array_features_training.append((util_classify.transform_document_in_dict(annotations, words_features, corpus), original_category))

    print "Training algorithm..."

    if kbest == 0:
        kbest = "all"

    pipeline = Pipeline([('chi2', SelectKBest(chi2, k=kbest)), ('tfidf', TfidfTransformer()),
                         ('svc', LinearSVC())])

    classifier = SklearnClassifier(pipeline)
    classifier.train(array_features_training)

    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []

    for (id, cat_original, annotations) in documents_test:
        cat_estimated = classifier.classify((util_classify.transform_document_in_dict(annotations, words_features, corpus)))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))
    return original_categories, estimated_categories


def linear_support_vector_machines_cross_language(corpus_training, corpus_test, documents_training, documents_test, words_features):
    """
    Cross Language linear Support Vector Machines algorithm. The Support Vector Machines algorithm with a linear kernel.
    An implementation of linear SVM to conduct cross-language experiments.
    :param corpus_training:
    :param corpus_test:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :return:
    """

    print
    print "----- Cross-Language Support Vector Machines algorithm------"
    print "Creating Training Vectors..."
    categories = util_classify.get_categories(corpus_training)
    ids_documents_test = []
    original_cats = []
    array_cats_names = []
    array_vector_training = []
    array_categories = []

    for (id, original_category, annotations) in documents_training:
        array_vector_training.append(util_classify.transform_document_in_vector(annotations, words_features, corpus_training))
        array_categories.append(util_classify.get_categories(corpus_training).index(original_category))

    for x in array_categories:
        array_cats_names.append(categories[x])
        
    print "Training the algorithm..."
    classifier = LinearSVC()

    X_train_features = []
    y_train_categories = []
    # Train all
    for (id, original_category, annotations) in documents_training:
        X_train_features.append(util_classify.transform_document_in_vector(annotations, words_features, corpus_training))
        y_train_categories.append(original_category)

    classifier.fit(np.array(X_train_features), np.array(y_train_categories))    

    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []

    categories = util_classify.get_categories(corpus_test)

    for (id, cat_original, annotations) in documents_test:
        ids_documents_test.append(id)
        original_cats.append(cat_original)
        cat_estimated = classifier.predict(np.array((util_classify.transform_document_in_vector(annotations, words_features, corpus_test))))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))

    categories_names = util_classify.get_categories(corpus_test)

    array_cats_names = []
    for x in estimated_categories:
        array_cats_names.append(categories_names[x])

    # Storage process predicted categories in DB
    util_classify.set_database_session(corpus_test)
    for document in Session.query(Document):
        if document.id in ids_documents_test:
            pos = ids_documents_test.index(document.id)
            document.classified_in_category = array_cats_names[pos]
    Session.commit()
    # End storage process predicted categories in DB

    return original_categories, estimated_categories

def linear_support_vector_machines_cross_language_hybrid(corpus_training, corpus_test, documents_training_bow, documents_test_bow, documents_training_boc, documents_test_boc, words_features):
    """
    Cross Language linear Support Vector Machines algorithm. The Support Vector Machines algorithm with a linear kernel.
    An implementation of linear SVM to conduct cross-language experiments.
    :param corpus_training:
    :param corpus_test:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :return:
    """

    print
    print "----- Cross-Language Support Vector Machines algorithm hybrid------"
    print "Creating Training Vectors..."
    categories = util_classify.get_categories(corpus_training)
    ids_documents_test = []
    original_cats = []
    array_cats_names = []
    array_vector_training = []
    array_categories = []


    for (id, original_category, annotations) in documents_training_bow:
        array_vector_training.append(util_classify.transform_document_in_vector(annotations, words_features, corpus_training))
        array_categories.append(util_classify.get_categories(corpus_training).index(original_category))

    for x in array_categories:
        array_cats_names.append(categories[x])

    print "Training the algorithm..."
    classifier = LinearSVC()

    X_train_features = []
    y_train_categories = []
    # Train all
    for (id, original_category, annotations) in documents_training_bow:
        X_train_features.append(util_classify.transform_document_in_vector(annotations, words_features, corpus_training))
        y_train_categories.append(original_category)

    classifier.fit(np.array(X_train_features), np.array(y_train_categories))

    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []

    categories = util_classify.get_categories(corpus_test)

    for (id, cat_original, annotations) in documents_test_bow:
        ids_documents_test.append(id)
        original_cats.append(cat_original)
        cat_estimated = classifier.predict(np.array((util_classify.transform_document_in_vector(annotations, words_features, corpus_test))))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))

    categories_names = util_classify.get_categories(corpus_test)

    array_cats_names = []
    for x in estimated_categories:
        array_cats_names.append(categories_names[x])

    # Storage process predicted categories in DB
    util_classify.set_database_session(corpus_test)
    for document in Session.query(Document):
        if document.id in ids_documents_test:
            pos = ids_documents_test.index(document.id)
            document.classified_in_category = array_cats_names[pos]
    Session.commit()
    # End storage process predicted categories in DB

    return original_categories, estimated_categories




def linear_support_vector_machines_cross_language_tf_idf(corpus_training, corpus_test, documents_training, documents_test, words_features, kbest):
    """
    Cross Language linear Support Vector Machines algorithm. The Support Vector Machines algorithm with a linear kernel.
    An implementation of linear SVM to conduct cross-language experiments.
    :param corpus_training:
    :param corpus_test:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :return:
    """

    print
    print "----- Cross-Language Support Vector Machines algorithm------"
    print "Creating Training Vectors..."
    categories = util_classify.get_categories(corpus_training)
    ids_documents_test = []
    original_cats = []
    array_cats_names = []
    array_features_training = []
    array_vector_training = []
    array_categories = []

    for (id, original_category, annotations) in documents_training:
        array_features_training.append((util_classify.transform_document_in_dict(annotations, words_features, corpus_training), original_category))
        array_categories.append(util_classify.get_categories(corpus_training).index(original_category))

    for x in array_categories:
        array_cats_names.append(categories[x])

    print "Training algorithm..."

    if kbest == 0:
        kbest = "all"

    pipeline = Pipeline([('chi2', SelectKBest(chi2, k=kbest)), ('tfidf', TfidfTransformer()), ('svc', LinearSVC())])

    classifier = SklearnClassifier(pipeline)
    classifier.train(array_features_training)

    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []

    categories = util_classify.get_categories(corpus_test)

    for (id, cat_original, annotations) in documents_test:
        cat_estimated = classifier.classify((util_classify.transform_document_in_dict(annotations, words_features, corpus_test)))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))

    '''
    categories_names = util_classify.get_categories(corpus_test)

    array_cats_names = []
    for x in estimated_categories:
        array_cats_names.append(categories_names[x])

    # Storage process predicted categories in DB
    util_classify.set_database_session(corpus_test)
    for document in Session.query(Document):
        if document.id in ids_documents_test:
            pos = ids_documents_test.index(document.id)
            document.classified_in_category = array_cats_names[pos]
    Session.commit()
    # End storage process predicted categories in DB
    '''

    return original_categories, estimated_categories


def nu_support_vector_machines(corpus, documents_training, documents_test, words_features, kernel, nu):
    """
    Another implementation of Support Vector Machines algorithm.
    :param corpus:
    :param documents_training:
    :param documents_test:
    :param words_features:
    :param kernel:
    :param nu:
    :return:
    """

    print
    print "----- nu-Support Vector Machines algorithm ------"
    print "Creating Training Vectors..."
    categories = util_classify.get_categories(corpus)  

    array_vector_training = []
    array_categories = []
    for (id, original_category, annotations) in documents_training:
        array_vector_training.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        array_categories.append(util_classify.get_categories(corpus).index(original_category))    
        
    print "Training the algorithm..."
    classifier = NuSVC(nu=nu, kernel=kernel)

    X_train_features = []
    y_train_categories = []
    # Train all
    for (id, original_category, annotations) in documents_training:
        X_train_features.append(util_classify.transform_document_in_vector(annotations, words_features, corpus))
        y_train_categories.append(original_category)

    classifier.fit(np.array(X_train_features), np.array(y_train_categories))    

    print "Calculating metrics..."
    estimated_categories = []
    original_categories = []

    for (id, cat_original, annotations) in documents_test:
        cat_estimated = classifier.predict(np.array((util_classify.transform_document_in_vector(annotations, words_features, corpus))))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))

    return original_categories, estimated_categories


'''
#################################################################################
################ PRUBAS VARIAS NO FUNCIONAL DE AQUI PARA ABAJO ##################
#################################################################################        

def extract_document_features(document,words_features):
    id ,cat_original, annotations = document
    corpus = "boc"
    document_features = {}  
    for annotation_name,total_weight in words_features.iteritems():
        if "boc" in corpus:
            document_features[annotation_name] =  util_classify.get_annotation_weight(annotation_name,annotations) #/float(total_weight)
        elif "bow" in corpus:
            document_features[annotation_name] =  annotations.count(annotation_name) #/float(total_weight)    
    return (document_features, cat_original)
   
                
def multinomial_bayes3(corpus, documents_training, documents_test, words_features,smoothing):             
    print
    print "----- ALGORITMO Multinomial Bayes ------"
    print "Creando Vectores features de training..."
        
    print documents_training
    #array_features_training = apply_features(extract_document_features,documents_training,words_features)
    array_features_training = list(LazyMap(extract_document_features, documents_training, words_features))
    
    
                
    #vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
    #X_train = vectorizer.fit_transform(data_train.data)
                    
    #array_features_training.append((util_classify.transform_document_in_dict(annotations,words_features,corpus),original_category))
    #y_train_categories = np.array([original_category])
    #X_train_features = np.array(util_classify.transform_document_in_vector(annotations,words_features))
    #tfidf_transformer = TfidfTransformer()        
    #X_train_tfidf_transformer = tfidf_transformer.fit_transform(X_train_features)
    
    print "Entrenando algoritmo..."
    #('chi2', SelectKBest(chi2, k=3000)),
    pipeline = Pipeline([('tfidf', TfidfTransformer()),                         
                         ('nb', MultinomialNB(alpha=smoothing))])
    classifier = SklearnClassifier(pipeline)
    classifier.train(array_features_training)

    
    print "Calculando metricas ..."
    categories = util_classify.get_categories(corpus)
    estimated_categories = []
    original_categories = []               
    
    for (id ,cat_original, annotations) in documents_test:
        cat_estimated = classifier.classify((util_classify.transform_document_in_dict(annotations,words_features,corpus)))
        estimated_categories.append(categories.index(cat_estimated))
        original_categories.append(categories.index(cat_original))
    return original_categories, estimated_categories
        
        
'''
