#!/usr/bin/env bash
cd ../../source
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 5 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 10 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 20 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 50 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 100 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 200 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 500 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 1000 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 2000 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_multilabel -method multilabel -train 5000 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC

python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 5 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 10 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 20 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 50 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 100 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 200 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 500 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 1000 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 2000 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_multilabel -method multilabel -train 5000 -test 5000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_multilabel_23_cats_test_5000 -algorithm linear_SVC
