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