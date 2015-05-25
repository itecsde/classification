#!/usr/bin/env bash
cd ../../source

python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 5 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 10 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 20 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 50 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 100 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 200 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 500 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc
python classify.py -corpus_training boc_wikipedia_spanish -corpus_test boc_wikipedia_spanish -method cross_language_linear_SVM -train 666 -test 166 -metric cosine -destination_folder train_wikipedia_spanish_test_wikipedia_spanish_166_test_boc



