#!/usr/bin/env bash
cd ../../source

python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 5 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 10 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 20 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 50 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 100 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 200 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 500 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 1000 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 2000 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus boc_ohsumed_randomized_multilabel -method multilabel -train 5000 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC

python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 5 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 10 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 20 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 50 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 100 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 200 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 500 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 1000 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 2000 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
python classify.py -corpus bow_ohsumed_randomized_multilabel -method multilabel -train 5000 -test 1000 -metric cosine -destination_folder linear_multilabel_SVC_ohsumed_randomized_multilabel -algorithm linear_SVC
