#!/usr/bin/env bash
cd ../../source

python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 5 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 10 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 20 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 50 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 100 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 200 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 500 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 1000 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 2000 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -kbest 0 -train 2398 -test 621 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_621_test_boc_kbest_0

