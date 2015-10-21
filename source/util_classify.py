import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scipy import spatial
import numpy as np
from numpy.linalg import pinv
from nltk.stem.porter import *
from nltk.tokenize import RegexpTokenizer
from db_simplified_declarative import Base, Document

EngineDB = None
DBSession = sessionmaker()
Session = DBSession()

def set_database_session(corpus):
    """
    Sets a database session
    :param corpus:
    :return: An opened session with the database associate to the input :param corpus:
    """
    global Sesionmaker, EngineDB, DBSession, Session
    
    if corpus == "boc_reuters_27000" or corpus == "bow_reuters_27000":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_27000_threshold_01'

    elif corpus == "boc_reuters_21578" or corpus == "bow_reuters_21578":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_21578_threshold_01'

    elif corpus == "boc_reuters_21578_expanded":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_21578_th_01_expanded'

    elif corpus == "boc_ohsumed" or corpus == "bow_ohsumed":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_threshold_01'

    elif corpus == "boc_ohsumed_expanded":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_th_01_expanded'
        
    elif corpus == "boc_20_newsgroup" or corpus == "bow_20_newsgroup":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_20newsgroups_threshold_01'

    elif corpus == "boc_20_newsgroup_expanded":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_20newsgroups_th_01_expanded'        
    
    elif corpus == "boc_ieee" or corpus == "bow_ieee":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ieee_threshould_01'

    elif corpus == "boc_ieee_expanded":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ieee_th_01_expanded'

    elif corpus == "bow_oercommons" or corpus == "boc_oercommons":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_oercommons_threshold_01'

    elif corpus == "bow_merlot" or corpus == "boc_merlot":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_merlot_threshold_01'

    elif corpus == "bow_ohsumed_multilabel" or corpus == "boc_ohsumed_multilabel":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_multilabel_threshold_01'

    elif corpus == "bow_uvigomed_multilabel" or corpus == "boc_uvigomed_multilabel":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_uvigomed_multilabel_threshold_01'

    elif corpus == "bow_uvigomed" or corpus == "boc_uvigomed":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_uvigomed_threshold_01'

    elif corpus == "bow_ohsumed_randomized" or corpus == "boc_ohsumed_randomized":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_randomized_threshold_01'

    elif corpus == "bow_ohsumed_randomized_multilabel" or corpus == "boc_ohsumed_randomized_multilabel":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_randomized_multilabel_threshold_01'

    elif corpus == "bow_reuters_rcv1" or corpus == "boc_reuters_rcv1":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_rcv1_threshold_01'

    elif corpus == "bow_reuters_rcv2" or corpus == "boc_reuters_rcv2":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_rcv2_threshold_01'

    elif corpus == "bow_reuters_rcv2_translated_to_english_google_translate" or corpus == "boc_reuters_rcv2_translated_to_english_google_translate":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_rcv2_translated_to_english_google_translate'

    elif corpus == "bow_wikipedia_english" or corpus == "boc_wikipedia_english":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_wikipedia_english_threshold_01'

    elif corpus == "bow_wikipedia_spanish" or corpus == "boc_wikipedia_spanish":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_wikipedia_spanish_annotations_translated_to_en_th_01'

    elif corpus == "bow_wikipedia_spanish_translated_to_english_google_translate" or corpus == "boc_wikipedia_spanish_translated_to_english_google_translate":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_wikipedia_es_translated_to_english_google_translate'

    elif corpus == "bow_wikipedia_human_medicine_english" or corpus == "boc_wikipedia_human_medicine_english":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_wikipedia_human_medicine_en'

    elif corpus == "bow_wikipedia_human_medicine_spanish" or corpus == "boc_wikipedia_human_medicine_spanish":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_wikipedia_human_medicine_es_annotations_en'

    elif corpus == "bow_wikipedia_human_medicine_spanish_to_english_google_translate" or corpus == "boc_wikipedia_human_medicine_spanish_to_english_google_translate":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_wikipedia_human_medicine_es_translated_to_en_GT'

    elif corpus == "bow_cnx" or corpus == "boc_cnx":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_cnx'

    elif corpus == "bow_oer_aggregator_oercommons" or corpus == "bow_oer_aggregator_merlot" or corpus == "bow_oer_aggregator_cnx":
        db_parameters = 'mysql://classify_user:classify_password@192.168.1.12/simplified_oer_aggregator'

    elif corpus == "bow_jrc_acquis_english" or corpus == "boc_jrc_acquis_english":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_jrc_acquis_en'

    elif corpus == "bow_jrc_acquis_spanish_to_english" or corpus == "boc_jrc_acquis_spanish_to_english":
        db_parameters = 'mysql://classify_user:classify_password@localhost/simplified_jrc_acquis_es_to_en'




    EngineDB = create_engine(db_parameters)
    Base.metadata.bind = EngineDB
    DBSession.configure(bind=EngineDB)    
    Session = DBSession()

def cosine_measure(v1,v2):
    """
    Calculates the cosine distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.cosine(v1,v2)

def jaccard_measure(v1,v2):
    """
    Calculates the Jaccard distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.jaccard(v1,v2)

def braycurtis_measure(v1,v2):
    """
    Calculates the Bray-Curtis distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.braycurtis(v1,v2)

def euclidean_measure(v1,v2):
    """
    Calculates the euclidean distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.euclidean(v1,v2)

def manhattan_measure(v1,v2):
    """
    Calculates the Manhattan distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.cityblock(v1,v2)

def chebyshev_measure(v1,v2):
    """
    Calculates the Chebyshev distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.chebyshev(v1,v2)

def seuclidean_measure(v1,v2):
    """
    Calculates the squared euclidean distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    V = np.var(v2)
    return spatial.distance.seuclidean(v1,v2,V)

def minkowski_measure(v1,v2):
    """
    Calculates the Minkowski distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    return spatial.distance.minkowski(v1,v2,2)

def mahalanobis_measure(v1,v2):
    """
    Calculates the Mahalanobis distance between two vectors v1 and v2).
    :param v1:
    :param v2:
    :return:
    """
    if (v1==v2).all() == True:
        return 0
    else:
        z = zip(v1,v2)
        cov_matrix = np.cov(z)
        inverse_cov_matrix = pinv(cov_matrix) #pinv avoid errors when matrix are singular
        return spatial.distance.mahalanobis(v1,v2,inverse_cov_matrix)

def get_categories(corpus):
    """
    Returns an array with the categories of a single-labeled corpus.
    :param corpus:
    :return:
    """
    return [category[0] for category in Session.query(Document.original_category).distinct()]              

def get_multiple_categories(corpus):
    """
    Return an array of unique categories of a multi-labeled corpus.
    :param corpus:
    :return:
    """
    categories = []

    if "oer_aggregator" in corpus:
        if "oercommons" in corpus:
            c_corpus = "oercommons"
        elif "merlot" in corpus:
            c_corpus= "merlot"
        elif "cnx" in corpus:
            c_corpus = "cnx"
        elif "wikipedia" in corpus:
            c_corpus = "wikipedia"
        for category in Session.query(Document.original_category).filter(Document.corpus == c_corpus).distinct():
            tokens = [x.strip() for x in category[0].split(',')]
            for i in tokens:
                categories.append(i)
        categories = list(set(categories))
        return categories
    else:
        for category in Session.query(Document.original_category).distinct():
            tokens = [x.strip() for x in category[0].split(',')]
            for i in tokens:
                categories.append(i)
        categories = list(set(categories))
        return categories

def get_document_annotations(annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting):
    """
    Returns the annotations of a document and its weight.
    :param annotations:
    :param weighting:
    :param threshold:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param expanded_weighting:
    :return:
    """

    if expansion_threshold < 1:
        expansion = True
    else:
        expansion = False
        
    aux_document_annotations = []
    for annotation in annotations:
        if annotation.weight >= threshold:
            if weighting == "milne":
                aux_weighting = annotation.weight
            elif weighting == "binary":
                aux_weighting = 1
            aux_document_annotations.append((annotation.name,aux_weighting))            
            if expansion == True and annotation.weight >= expansion_threshold:                
                for annotation_expanded in annotations:                   
                    if annotation_expanded.expanded == True and annotation_expanded.expanded_from == annotation.old_id and annotation_expanded.relatedness >= expansion_relatedness:
                        aux_document_annotations.append((annotation_expanded.name,expanded_weighting))
    return aux_document_annotations


def annotations_to_words (annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting):
    """
    Returns the annotations of a document and its weight.
    :param annotations:
    :param weighting:
    :param threshold:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param expanded_weighting:
    :return:
    """

    if expansion_threshold < 1:
        expansion = True
    else:
        expansion = False

    aux_document_annotations = []
    for annotation in annotations:
        if annotation.weight >= threshold:
            if weighting == "milne":
                aux_weighting = annotation.weight
            elif weighting == "binary":
                aux_weighting = 1
            aux_document_annotations.append(annotation.name.decode(encoding="ISO-8859-1"))
            if expansion == True and annotation.weight >= expansion_threshold:
                for annotation_expanded in annotations:
                    if annotation_expanded.expanded == True and annotation_expanded.expanded_from == annotation.old_id and annotation_expanded.relatedness >= expansion_relatedness:
                        aux_document_annotations.append(annotation_expanded.name.decode(encoding="ISO-8859-1"))
    return aux_document_annotations

def get_documents_from_database_boc(corpus, threshold, weighting, expansion_threshold, expansion_relatedness, num_documents_per_category_for_training ,expanded_weighting, num_documents_per_category_for_testing = 0):
    """
    Obtain the first BoC :param num_documents_per_category_for_training: training documents per category
    and the first BoC :param num_documents_per_category_for_testing: test documents from the :param corpus: corpus.
    :param corpus:
    :param threshold:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param num_documents_per_category_for_training:
    :param expanded_weighting:
    :param num_documents_per_category_for_testing:
    :return:
    """

    print "--- METHOD: get_documents_from_database_boc() ---"
    documents_train = []
    documents_test = []
        
    if "reuters_27000" in corpus or "ieee" in corpus:
        categories = get_categories(corpus)
        ubicacion = categories.index("General Topics for Engineers .LB.Math  Science .AND. Engineering.RB.")
        del categories[ubicacion]
        for category in categories:
            total_documents_by_category = Session.query(Document).filter(Document.original_category == category).count()        
            for document in Session.query(Document).filter(Document.original_category == category)[:num_documents_per_category_for_training]:
                documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting)))
                # documents_train.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
                                       
            if num_documents_per_category_for_testing > 0:          
                for document in Session.query(Document).filter(Document.original_category == category)[total_documents_by_category - num_documents_per_category_for_testing: total_documents_by_category]:#num_documents_per_category_for_training:num_documents_per_category_for_training+num_documents_per_category_for_testing]:
                    documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
                    
        if num_documents_per_category_for_testing == 0:
            return documents_train
        else:   
            return documents_train, documents_test
    else:
        categories = get_categories(corpus)     
        # Training
        if num_documents_per_category_for_training == 0:
            print "Obtaining training documents from complete corpus " + corpus
            for document in Session.query(Document).filter(Document.cgisplit == "train"):
                documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness)))                 
                # documents_train.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
        else:
            print "Obtaining training documents from a part of corpus " + corpus
            num_train = 0 
            for category in categories:
                for document in Session.query(Document).filter(Document.original_category == category).filter(Document.cgisplit == "train"):
                    documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting)))                                
                    if num_train >= num_documents_per_category_for_training:
                        break;
                    else:
                        num_train+=1
                num_train = 0
        # Test
        if num_documents_per_category_for_testing == 0:                
            print "Obtaining test documents from complete corpus " + corpus
            for document in Session.query(Document).filter(Document.cgisplit == "test"):
                if weighting == "milne":
                    documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
                elif weighting == "binary":
                    documents_test.append((document.id, document.original_category, [(annotation.name,1) for annotation in document.annotations if annotation.weight >= threshold]))
        else:
            print "Obtaining test documents from a part of corpus " + corpus
            num_test = 0
            for category in categories:
                for document in Session.query(Document).filter(Document.original_category == category).filter(Document.cgisplit == "test"):
                    if weighting == "milne":                                                         
                        documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
                    elif weighting == "binary":
                        documents_test.append((document.id, document.original_category, [(annotation.name,1) for annotation in document.annotations if annotation.weight >= threshold]))
                    if num_test >= num_documents_per_category_for_testing:
                        break;
                    else:
                        num_test+=1
                num_test = 0     
                       
        return documents_train, documents_test

def get_documents_from_cross_language_database_boc(corpus_training, corpus_test,threshold, weighting, expansion_threshold, expansion_relatedness, num_documents_for_training, expanded_weighting, num_documents_for_test):
    """
    Obtain :param num_documents_for_training: BoC random training documents from :param corpus_training: training corpus
    and :param num_documents_for_test: BoC random test documents from :param corpus_test: test corpus
    :param corpus_training:
    :param corpus_test:
    :param threshold:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param num_documents_for_training:
    :param expanded_weighting:
    :param num_documents_for_test:
    :return:
    """

    print "--- Method: get_documents_from_cross_language_database_boc() ---"

    documents_train = []
    documents_test = []

    # Training
    set_database_session(corpus_training)
    if num_documents_for_training == 0:
        print "Obtaining training documents from complete corpus  " + corpus_training
        for document in Session.query(Document).filter(Document.cgisplit == "train"):
            documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting)))                 
        random.seed("www.itec-sde.net")
        random.shuffle(documents_train)
    else:
        print "Obtaining training documents from a part of corpus  " + corpus_training
        for document in Session.query(Document).filter(Document.cgisplit == "train").filter(Document.id < 10):
            documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting)))                                
        random.seed("www.itec-sde.net")
        random.shuffle(documents_train)
        documents_train = documents_train[0:num_documents_for_training]

    # Test
    set_database_session(corpus_test)
    if num_documents_for_test == 0:                
        print "Obtaining test documents from complete corpus " + corpus_test
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            if weighting == "milne":
                documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
            elif weighting == "binary":
                documents_test.append((document.id, document.original_category, [(annotation.name,1) for annotation in document.annotations if annotation.weight >= threshold]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)
    else:
        print "Obtaining test documents from a part of corpus " + corpus_test
        for document in Session.query(Document).filter(Document.cgisplit == "test").filter(Document.id < 10):
            if weighting == "milne":                                                      
                documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
            elif weighting == "binary":
                documents_test.append((document.id, document.original_category, [(annotation.name,1) for annotation in document.annotations if annotation.weight >= threshold]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)   
        documents_test = documents_test[0:num_documents_for_test]
        #print documents_test[0]
                   
    return documents_train, documents_test

def add_concepts_to_bow_document(document, weight):
    for annotation in document.annotations:
        for i in range(0, weight):
            document.description = document.description + annotation.name + " "
    return document

def get_documents_from_cross_language_database_bow(corpus_training, corpus_test, hybrid, threshold, weighting, expansion_threshold, expansion_relatedness, num_documents_for_training, expanded_weighting, num_documents_for_test):
    """
    Obtain :param num_documents_for_training: BoW random training documents from :param corpus_training: training corpus
    and :param num_documents_for_test: BoW random test documents from :param corpus_test: test corpus
    :param corpus_training:
    :param corpus_test:
    :param threshold:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param num_documents_for_training:
    :param expanded_weighting:
    :param num_documents_for_test:
    :return:
    """

    print "--- METHOD: get_documents_from_cross_language_database_bow() ---"
    
    stemmer = PorterStemmer()
    tokenizer =  RegexpTokenizer(r'\w+')
    documents_training = []
    documents_test = []

    # Training
    set_database_session(corpus_training)   
    if num_documents_for_training == 0:
        print "Obtaining training documents from complete corpus " + corpus_training
        for document in Session.query(Document).filter(Document.cgisplit == "train"):
            documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_training)
    else:
        print "Obtaining training documents from a part of the corpus " + corpus_training
        for document in Session.query(Document).filter(Document.cgisplit == "train"):                    
            if hybrid == "yes":
                documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))] + annotations_to_words(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting) ))
            elif hybrid == "no":
                documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_training)
        documents_training = documents_training[0:num_documents_for_training]

    # Test
    set_database_session(corpus_test)
    if num_documents_for_test == 0:
        print "Obtaining test documents from complete corpus " + corpus_test
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)
    else:
        print "Obtaining test documents from a part of the corpus " + corpus_test
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            if hybrid == "yes":
                documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))] + annotations_to_words(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting) ))
            elif hybrid == "no":
                documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)   
        documents_test = documents_test[0:num_documents_for_test]
        
    return documents_training, documents_test

def get_documents_from_database_bow(corpus, num_documents_per_category_for_training,num_documents_per_category_for_test = 0):
    """
    Obtain the first BoW :param num_documents_per_category_for_training: training documents per category
    and the first BoW :param num_documents_per_category_for_testing: test documents from the :param corpus: corpus.
    :param corpus:
    :param num_documents_per_category_for_training:
    :param num_documents_per_category_for_test:
    :return:
    """

    print "--- METHOD: get_documents_from_database_bow() ---"
    
    stemmer = PorterStemmer()
    tokenizer =  RegexpTokenizer(r'\w+')
    documents_training = []
    documents_test = []       
         
    if "reuters_27000" in corpus or "ieee" in corpus:
        categories = get_categories(corpus)
        ubicacion = categories.index("General Topics for Engineers .LB.Math  Science .AND. Engineering.RB.")
        del categories[ubicacion]
        print "Obtaining training and test documents from complete corpus " + corpus
        for category in categories:
            total_documents_by_category = Session.query(Document).filter(Document.original_category == category).count()
            for document in Session.query(Document).filter(Document.original_category == category)[:num_documents_per_category_for_training]:            
                try:            
                    documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(str(document.name) + "." + document.description)]))            
                except ValueError:
                    continue
                                                   
            if num_documents_per_category_for_test > 0:          
                for document in Session.query(Document).filter(Document.original_category == category)[total_documents_by_category - num_documents_per_category_for_test: total_documents_by_category]:
                    try:
                        documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(str(document.name) + "." + document.description)]))                                
                    except ValueError:
                        continue
    
        if num_documents_per_category_for_test == 0:
            return documents_training
        else:   
            return documents_training, documents_test
        
    # Rest of corpora
    else:
        categories = get_categories(corpus)        
        # Training
        if num_documents_per_category_for_training == 0:
            print "Obtaining training documents from complete corpus" + corpus
            for document in Session.query(Document).filter(Document.cgisplit == "train"):                    
                documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))] ))
        else:
            num_train = 0
            print "Obtaining training documents from a part of the corpus " + corpus
            for category in categories:
                for document in Session.query(Document).filter(Document.original_category == category).filter(Document.cgisplit == "train"):                    
                    documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))                    
                    if num_train >= num_documents_per_category_for_training:
                        break;
                    else:
                        num_train+=1
                num_train = 0
        #Test
        if num_documents_per_category_for_test == 0:
            print "Obtaining test documents from complete corpus " + corpus
            for document in Session.query(Document).filter(Document.cgisplit == "test"):
                documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        else:
            num_test = 0
            print "Obtaining test documents from a part or the corpus " + corpus
            for category in categories:     
                for document in Session.query(Document).filter(Document.original_category == category).filter(Document.cgisplit == "test"):
                    documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))                    
                    if num_test >= num_documents_per_category_for_test:
                        break;
                    else:
                        num_test+=1               
                num_test = 0 
            
        return documents_training, documents_test

def get_documents_from_multilabel_database_boc(corpus,threshold, weighting, expansion_threshold, expansion_relatedness, num_documents_for_training, expanded_weighting, num_documents_for_test = 0):
    """
    Obtain :param num_documents_for_training: BoC random training documents from :param corpus: corpus
    and :param num_documents_for_test: BoC random test documents from :param corpus: corpus
    :param corpus:
    :param threshold:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param num_documents_for_training:
    :param expanded_weighting:
    :param num_documents_for_test:
    :return:
    """
    print "--- METHOD: get_documents_from_multilabel_database_boc() ---"
    documents_train = []
    documents_test = []

    # Train
    if num_documents_for_training == 0:
        print "Obtaining training documents from complete corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "train"):
            documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting)))                 
        random.seed("www.itec-sde.net")
        random.shuffle(documents_train)
    else:
        print "Obtaining training documents from a part of the corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "train"):
            documents_train.append((document.id, document.original_category, get_document_annotations(document.annotations, weighting, threshold, expansion_threshold, expansion_relatedness, expanded_weighting)))                                
        random.seed("www.itec-sde.net")
        random.shuffle(documents_train)
        documents_train = documents_train[0:num_documents_for_training]

    # Test
    if num_documents_for_test == 0:                
        print "Obtaining test documents from complete corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            if weighting == "milne":
                documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
            elif weighting == "binary":
                documents_test.append((document.id, document.original_category, [(annotation.name,1) for annotation in document.annotations if annotation.weight >= threshold]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)
    else:
        print "Obtaining training documents from a part of the corpus " + corpus
        num_test = 0
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            if weighting == "milne":                                                         
                documents_test.append((document.id, document.original_category, [(annotation.name,annotation.weight) for annotation in document.annotations if annotation.weight >= threshold]))
            elif weighting == "binary":
                documents_test.append((document.id, document.original_category, [(annotation.name,1) for annotation in document.annotations if annotation.weight >= threshold]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)   
        documents_test = documents_test[0:num_documents_for_test]
                   
    return documents_train, documents_test

def add_metadata_to_document(document, metadata_freq):
    for annotation in document.annotations:
        for i in range(0,metadata_freq):
            document.description = document.description + annotation.name.replace(" ", "_") + " "
    return document


def get_documents_from_multilabel_database_bow_cross_corpora(corpus_training, corpus_test, num_documents_for_training, metadata, metadata_freq, num_documents_for_test = 0):
    """
    Obtain :param num_documents_for_training: BoW random training documents from :param corpus: corpus
    and :param num_documents_for_test: BoW random test documents from :param corpus: corpus
    :param corpus:
    :param num_documents_for_training:
    :param metadata:
    :param metadata_freq:
    :param num_documents_for_test:
    :return:
    """
    print "--- METHOD: get_documents_from_multilabel_database_bow_cross_corpora() ---"

    if "oercommons" in corpus_training:
        c_train = "oercommons"
    elif "merlot" in corpus_training:
        c_train = "merlot"
    elif "cnx" in corpus_training:
        c_train = "cnx"
    elif "wikipedia" in corpus_training:
        c_train = "wikipedia"

    if "oercommons" in corpus_test:
        c_test = "oercommons"
    elif "merlot" in corpus_test:
        c_test = "merlot"
    elif "cnx" in corpus_test:
        c_test = "cnx"
    elif "wikipedia" in corpus_test:
        c_test = "wikipedia"


    stemmer = PorterStemmer()
    tokenizer =  RegexpTokenizer(r'\w+')
    documents_training = []
    documents_test = []

    print "metadata: " + metadata
    print "freq: " + str(metadata_freq)

    # Train
    set_database_session(corpus_training)
    if num_documents_for_training == 0:
        print "Obtaining training documents from complete corpus " + corpus_training
        for document in Session.query(Document).filter(Document.corpus == c_train).filter(Document.cgisplit == "train"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)
            documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))] ))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_training)
    else:
        print "Obtaining training documents from a part of the corpus " + corpus_training
        for document in Session.query(Document).filter(Document.corpus == c_train).filter(Document.cgisplit == "train"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)
            documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_training)
        documents_training = documents_training[0:num_documents_for_training]

    # Test
    set_database_session(corpus_test)
    if num_documents_for_test == 0:
        print "Obtaining test documents from complete corpus " + corpus_test
        for document in Session.query(Document).filter(Document.corpus == c_test).filter(Document.cgisplit == "test"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)
            documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)
    else:
        print "Obtaining test documents from a part of the corpus " + corpus_test
        for document in Session.query(Document).filter(Document.corpus == c_test).filter(Document.cgisplit == "test"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)
            documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)
        documents_test = documents_test[0:num_documents_for_test]

    return documents_training, documents_test



def get_documents_from_multilabel_database_bow(corpus, num_documents_for_training, metadata, metadata_freq, num_documents_for_test = 0):
    """
    Obtain :param num_documents_for_training: BoW random training documents from :param corpus: corpus
    and :param num_documents_for_test: BoW random test documents from :param corpus: corpus
    :param corpus:
    :param num_documents_for_training:
    :param metadata:
    :param metadata_freq:
    :param num_documents_for_test:
    :return:
    """
    print "--- METHOD: get_documents_from_multilabel_database_bow() ---"
    
    stemmer = PorterStemmer()
    tokenizer =  RegexpTokenizer(r'\w+')
    documents_training = []
    documents_test = []

    print "metadata: " + metadata
    print "freq: " + str(metadata_freq)

    # Train
    if num_documents_for_training == 0:
        print "Obtaining training documents from complete corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "train"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)
            documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))] ))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_training)
    else:
        print "Obtaining training documents from a part of the corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "train"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)
            documents_training.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_training)
        documents_training = documents_training[0:num_documents_for_training]
    
    # Test
    if num_documents_for_test == 0:
        print "Obtaining test documents from complete corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)            
            documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)
    else:
        print "Obtaining test documents from a part of the corpus " + corpus
        for document in Session.query(Document).filter(Document.cgisplit == "test"):
            if metadata == "yes":
                add_metadata_to_document(document, metadata_freq)            
            documents_test.append((document.id, document.original_category, [stemmer.stem(word_stem) for word_stem in tokenizer.tokenize(document.description.decode(encoding="ISO-8859-1"))]))
        random.seed("www.itec-sde.net")
        random.shuffle(documents_test)   
        documents_test = documents_test[0:num_documents_for_test]
        
    return documents_training, documents_test


def get_unique_words_boc(documents):
    """
    Returns a list of unique words of all documents and the total weight of each
    :param documents:
    :return:
    """
    print "--- METHOD: get_unique_words_boc() ---"
    words_with_duplicates = []
    words_features = {}

    for (id, cat, annotations) in documents:
        for (annotation_name, annotation_weight) in annotations:
            words_with_duplicates.append(annotation_name.decode(encoding="ISO-8859-1"))
    
    words_unique = list(set(words_with_duplicates))
    
    for word in words_unique:
        for (id, cat, annotations) in documents:
            for (annotation_name, annotation_weight) in annotations:
                if annotation_name.decode(encoding="ISO-8859-1") == word:
                    if words_features.has_key(word):
                        # le pongo uno para ver si asi influye el boc
                        #words_features[word] += 1
                        words_features[word] += annotation_weight
                    else:
                        # le pongo uno para ver si asi influye el boc
                        #words_features[word] = 1
                        words_features[word] = annotation_weight

    return words_features

def get_unique_words_bow(documents):
    """
     Returns a list of unique words of all documents and the number of appearances in total in all documents
    :param documents:
    :return:
    """
    print "--- METHOD: get_unique_words_bow() ---"
    words_with_duplicates = []
    words_features = {}    
    for (id, cat, list_words) in documents:
        for (word) in list_words:
            words_with_duplicates.append(word)
        
    words_unique = list(set(words_with_duplicates))

    for word in words_unique:
        words_features[word] = 1
    return words_features
    

def transform_document_in_vector(annotations, words_features,corpus):
    """
    Transform the document into a weighted list of features
    :param annotations:
    :param words_features:
    :param corpus:
    :return:
    """
    document_vector = []    
    for annotation_name,total_weight in words_features.iteritems():
        if "boc" in corpus:        
            document_vector.append(get_annotation_weight(annotation_name,annotations)) #/float(total_weight))
        elif "bow" in corpus:
            document_vector.append(annotations.count(annotation_name)) #/float(total_weight)
    return document_vector


def transform_document_in_dict(annotations, words_features,corpus):
    """
    Transform the document in a dictionary composed by the couples: word that refers and weight in the particular document.
    :param annotations:
    :param words_features:
    :param corpus:
    :return:
    """
    document_features = {}    
    for annotation_name,total_weight in words_features.iteritems():
        if "boc" in corpus:
            document_features[annotation_name] =  get_annotation_weight(annotation_name,annotations) #/float(total_weight)
        elif "bow" in corpus:
            document_features[annotation_name] =  annotations.count(annotation_name) #/float(total_weight)    
    return document_features


def get_annotation_weight(annotation_name, annotations):
    """
    Return the weight of an annotation.
    :param annotation_name:
    :param annotations:
    :return:
    """
    for (name, weight) in annotations:
        if name == annotation_name:
            return weight
    return 0


def print_experiment_details(corpus, corpus_training, corpus_test, threshold,number_of_documents_for_training, number_of_documents_for_testing, classify_method, tfidf, stemming, smoothing, weighting, expansion_threshold, expansion_relatedness, expanded_weighting, neighbors, metric, algorithm, kernel, nu):
    """
    Print the details of an experiment.
    :param corpus:
    :param corpus_training:
    :param corpus_test:
    :param threshold:
    :param number_of_documents_for_training:
    :param number_of_documents_for_testing:
    :param classify_method:
    :param tfidf:
    :param stemming:
    :param smoothing:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param expanded_weighting:
    :param neighbors:
    :param metric:
    :param algorithm:
    :param kernel:
    :param nu:
    :return:
    """
    print "---- EXPERIMENT DETAILS ----"
    if corpus == "cross_language":
        print "CORPUS TRAINING: " + corpus_training.replace("bow_", "").replace("boc_", "")
        print "CORPUS TEST: " + corpus_test.replace("bow_", "").replace("boc_", "")
        if "bow" in corpus_training and "bow" in corpus_test:
            print "REPRESENTATION: BoW" 
        elif "boc" in corpus_training and "boc" in corpus_test:
            print "REPRESENTATION: BoC" 
    else:
        print "CORPUS: " + corpus.replace("bow_", "").replace("boc_", "")
        if "bow" in corpus:
            print "REPRESENTATION: BoW" 
        else:
            print "REPRESENTATION: BoC"   
 
    print "THRESHOLD: " + str(threshold)
    if "boc" in corpus:
        if expansion_threshold != 1 and expansion_relatedness != 1:
            print "EXPANSION THRESHOLD: " + str(expansion_threshold)
            print "EXPANSION RELATEDNESS: " + str(expansion_relatedness)
            print "EXPANDED WEIGHTING: " + str(expanded_weighting) 
                     
    print "CLASSIFY METHOD: " + classify_method
    print "METRIC: " + metric
    if tfidf == True:
        print "TFIDF: yes"                            
    else:
        print "TFIDF: no"
    if classify_method == "kneighbors":
        print "NEIGHBORS: " + str(neighbors)
    if "bow" in corpus:
        print "STEMMING: " + stemming
    else:
        print "STEMMING: -"
    print "SMOOTHING: " + str(smoothing)
    print "WEIGHTING: " + weighting

    if classify_method == "multilabel":
        print "ALGORITHM: " + algorithm

    if classify_method == "SVM" or classify_method == "nu_SVM":
        print "KERNEL FUNCTION: " + kernel

    if classify_method == "nu_SVM":
        print "NU: " + str(nu)
 
    if number_of_documents_for_training == 0:
        print "#TRAIN: all"       
    else:
        print "#TRAIN: " + str(number_of_documents_for_training)
        
    if number_of_documents_for_testing == 0:
        print "#TEST: all"
    else:
        print "#TEST: " + str(number_of_documents_for_testing)
    print

def get_experiment_results(corpus, threshold,number_of_documents_for_training, number_of_documents_for_testing, classify_method, tfidf, stemming, smoothing, weighting, expansion_threshold, expansion_relatedness, f1_score, expanded_weighting, kbest, n_neighbors, metric, kernel, nu, precision, recall):
    """
    Get the results of an experiment and write them into a .json file.
    :param corpus:
    :param threshold:
    :param number_of_documents_for_training:
    :param number_of_documents_for_testing:
    :param classify_method:
    :param tfidf:
    :param stemming:
    :param smoothing:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param f1_score:
    :param expanded_weighting:
    :param kbest:
    :param n_neighbors:
    :param metric:
    :param kernel:
    :param nu:
    :param precision:
    :param recall:
    :return:
    """
    c_corpus = corpus.replace("bow_","").replace("boc_", "")
    if "bow" in corpus:
        c_representation = "BoW"
    else:
        c_representation = "BoC"    
    
    if "boc" in corpus and expansion_threshold != 1 and expansion_relatedness != 1:
        
        c_expansion_threshold = expansion_threshold
        c_expansion_relatedness = expansion_relatedness
        c_expanded_weighting = expanded_weighting
    else:
        c_expansion_threshold = None
        c_expansion_relatedness = None
        c_expanded_weighting = None

    if classify_method == "SVM" or classify_method == "nu_SVM":
        c_kernel = kernel
    else:
        c_kernel = None

    if classify_method == "nu_SVM":
        c_nu = nu
    else:
        c_nu = None
           
    content = {'corpus': c_corpus, 'representation': c_representation, 'threshold': threshold, 'expansion_threshold': c_expansion_threshold, 'expansion_relatedness': c_expansion_relatedness,'classify_method': classify_method, 'tfidf': tfidf, 'stemming': stemming, 'smoothing': smoothing, 'weighting': weighting, 'train': number_of_documents_for_training, 'test': number_of_documents_for_testing, 'f1_score': f1_score, 'expanded_weighting': c_expanded_weighting , 'KBest': kbest, 'n_neighbors': n_neighbors, 'metric': metric, 'kernel': c_kernel, 'nu': c_nu, 'precision': precision, 'recall': recall}
    
    return content
    
def get_experiment_multilabel_results(corpus, threshold,number_of_documents_for_training, number_of_documents_for_testing, classify_method, tfidf ,stemming, smoothing, weighting, expansion_threshold, expansion_relatedness, f1_score, expanded_weighting, kbest, n_neighbors, metric, hamming_loss, accuracy, precision, recall, algorithm, metadata_weight):
    """
    Get the results of an multilabel experiment and write them into a .json file.
    :param corpus:
    :param threshold:
    :param number_of_documents_for_training:
    :param number_of_documents_for_testing:
    :param classify_method:
    :param tfidf:
    :param stemming:
    :param smoothing:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param f1_score:
    :param expanded_weighting:
    :param kbest:
    :param n_neighbors:
    :param metric:
    :param hamming_loss:
    :param accuracy:
    :param precision:
    :param recall:
    :param algorithm:
    :return:
    """
    c_corpus = corpus.replace("bow_","").replace("boc_","")
    if "bow" in corpus:
        c_representation = "BoW"
    else:
        c_representation = "BoC"    
    
    if "boc" in corpus and expansion_threshold != 1 and expansion_relatedness != 1:
        
        c_expansion_threshold = expansion_threshold
        c_expansion_relatedness = expansion_relatedness
        c_expanded_weighting = expanded_weighting
    else:
        c_expansion_threshold = None
        c_expansion_relatedness = None
        c_expanded_weighting = None
           
    content = {'corpus': c_corpus, 'representation': c_representation, 'threshold': threshold,
               'expansion_threshold': c_expansion_threshold, 'expansion_relatedness': c_expansion_relatedness,
               'classify_method': classify_method, 'tfidf': tfidf, 'stemming': stemming, 'smoothing': smoothing,
               'weighting': weighting, 'train': number_of_documents_for_training,
               'test': number_of_documents_for_testing, 'f1_score': f1_score,
               'expanded_weighting': c_expanded_weighting , 'KBest': kbest, 'n_neighbors': n_neighbors,
               'metric': metric, 'hamming_loss': hamming_loss, 'accuracy': accuracy, 'precision': precision,
               'recall': recall, 'algorithm': algorithm, 'metadata_weight': metadata_weight}
    
    return content
    

def get_experiment_cross_language_results(corpus, corpus_training, corpus_test, threshold,number_of_documents_for_training, number_of_documents_for_testing, classify_method, tfidf, stemming, smoothing, weighting, expansion_threshold, expansion_relatedness, f1_score, expanded_weighting, kbest, n_neighbors, metric, kernel, nu, precision, recall, hybrid):
    """
    Get the results of an cross-language experiment and write them into a .json file.
    :param corpus:
    :param corpus_training:
    :param corpus_test:
    :param threshold:
    :param number_of_documents_for_training:
    :param number_of_documents_for_testing:
    :param classify_method:
    :param tfidf:
    :param stemming:
    :param smoothing:
    :param weighting:
    :param expansion_threshold:
    :param expansion_relatedness:
    :param f1_score:
    :param expanded_weighting:
    :param kbest:
    :param n_neighbors:
    :param metric:
    :param kernel:
    :param nu:
    :param precision:
    :param recall:
    :return:
    """
    c_corpus = corpus.replace("bow_","").replace("boc_","")
    c_corpus_training = corpus_training.replace("bow_","").replace("boc_","")
    c_corpus_test = corpus_test.replace("bow_","").replace("boc_","")

    if "bow" in corpus_training and "bow" in corpus_test:
        c_representation = "BoW"
    elif "boc" in corpus_training and "boc" in corpus_test:
        c_representation = "BoC"    
    
    if "boc" in corpus_training and "boc" in corpus_test and expansion_threshold != 1 and expansion_relatedness != 1:
        
        c_expansion_threshold = expansion_threshold
        c_expansion_relatedness = expansion_relatedness
        c_expanded_weighting = expanded_weighting
    else:
        c_expansion_threshold = None
        c_expansion_relatedness = None
        c_expanded_weighting = None
           
    content = {'corpus': c_corpus, 'corpus_training': c_corpus_training, 'corpus_test': c_corpus_test, 'representation': c_representation, 'threshold': threshold, 'expansion_threshold': c_expansion_threshold, 'expansion_relatedness': c_expansion_relatedness,'classify_method': classify_method, 'tfidf': tfidf, 'stemming': stemming, 'smoothing': smoothing, 'weighting': weighting, 'train': number_of_documents_for_training, 'test': number_of_documents_for_testing, 'f1_score': f1_score, 'expanded_weighting': c_expanded_weighting , 'KBest': kbest, 'n_neighbors': n_neighbors, 'metric': metric, 'precision': precision, 'recall': recall, 'hybrid': hybrid}
    
    return content