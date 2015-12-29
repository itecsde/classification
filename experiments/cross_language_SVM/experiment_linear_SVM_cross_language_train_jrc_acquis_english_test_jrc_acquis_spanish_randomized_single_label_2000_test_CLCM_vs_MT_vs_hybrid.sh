#!/usr/bin/env bash
cd ../../source

#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 10 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 20 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 50 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 100 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 200 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 500 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 1000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method  -train 2000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_MT

#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 10 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 20 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 50 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 100 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 200 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 500 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 1000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 2000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM
#python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_CLCM

#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 10 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 20 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 50 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 100 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 200 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 500 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 1000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 2000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes
#python classify.py -corpus_training bow_jrc_acquis_english -corpus_test bow_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_hybrid -hybrid yes

python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 10 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 20 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 50 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 100 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 200 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 500 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 1000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 2000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection
python classify.py -corpus_training boc_jrc_acquis_english -corpus_test boc_jrc_acquis_spanish_to_english -method multilabel_cross_language_linear_SVM -train 5000 -test 2000 -metric cosine -destination_folder train_jrc_acquis_en_test_jrc_acquis_es_2000_test_feature_selection