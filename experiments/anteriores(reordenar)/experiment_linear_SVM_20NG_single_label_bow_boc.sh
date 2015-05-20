#!/usr/bin/env bash
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 5 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 10 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 15 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 20 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 25 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 30 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 40 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 50 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 75 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 100 -destination_folder linear_SVM_20_newsgroup_SL_SL
#python classify.py -corpus bow_20_newsgroup -method linear_SVM  -train 150 -destination_folder linear_SVM_20_newsgroup_SL_SL

#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 5 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 10 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 15 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 20 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 25 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 30 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 40 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 50 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 75 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 100 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01
#python classify.py -corpus boc_20_newsgroup -method linear_SVM -threshold 0.10 -train 150 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01


python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 5  -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 10 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 15 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 20 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 25 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 30 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 40 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 50 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 75 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 100 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
python classify.py -corpus bow_20_newsgroup -method linear_SVM -kbest 0 -train 150 -destination_folder linear_SVM_20_newsgroup_SL_SL_th_01_tfidf_true
