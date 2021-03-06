#!/usr/bin/env bash
cd ../../source

python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 5 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 10 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 20 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 50 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 100 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 200 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 500 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 1000 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 2000 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc
python classify.py -corpus_training boc_wikipedia_english -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 3000 -test 832 -metric cosine -destination_folder train_wikipedia_english_test_wikipedia_spanish_832_test_boc

