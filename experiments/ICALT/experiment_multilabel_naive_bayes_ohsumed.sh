#!/usr/bin/env bash
cd ../../source
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 5 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 10 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 20 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 50 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 100 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 200 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 500 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 1000 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 2000 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 5000 -test 1000 -metric cosine -destination_folder multilabel_naive_bayes_ohsumed_multilabel -algorithm Bayes
