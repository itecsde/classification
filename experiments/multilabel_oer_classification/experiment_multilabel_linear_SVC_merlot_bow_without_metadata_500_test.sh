#!/usr/bin/env bash
cd ../../source

python classify.py -corpus bow_merlot -method multilabel -train 5 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 10 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 20 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 50 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 100 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 200 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 500 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 1000 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 2000 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
python classify.py -corpus bow_merlot -method multilabel -train 5000 -test 500 -metric cosine -destination_folder linear_multilabel_SVC_merlot_multilabel_bow_without_metadata -algorithm linear_SVC
