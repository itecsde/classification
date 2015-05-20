#!/usr/bin/env bash
python classify.py -method multilabel -corpus bow_oercommons -train 11000 -test 100 -metric cosine -destination_folder multilabel_mas
python classify.py -method multilabel -corpus bow_oercommons -train 11000 -test 200 -metric cosine -destination_folder multilabel_mas
python classify.py -method multilabel -corpus bow_oercommons -train 11000 -test 500 -metric cosine -destination_folder multilabel_mas
python classify.py -method multilabel -corpus bow_oercommons -train 11000 -test 1000 -metric cosine -destination_folder multilabel_mas
python classify.py -method multilabel -corpus bow_oercommons -train 11000 -test 2000 -metric cosine -destination_folder multilabel_mas

#python classify.py -method multilabel -corpus bow_oercommons -train 12000 -test 100 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 12000 -test 200 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 12000 -test 500 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 12000 -test 1000 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 12000 -test 2000 -metric cosine -destination_folder multilabel_mas

#python classify.py -method multilabel -corpus bow_oercommons -train 13000 -test 100 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 13000 -test 200 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 13000 -test 500 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 13000 -test 1000 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 13000 -test 2000 -metric cosine -destination_folder multilabel_mas

#python classify.py -method multilabel -corpus bow_oercommons -train 14000 -test 100 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 14000 -test 200 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 14000 -test 500 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 14000 -test 1000 -metric cosine -destination_folder multilabel_mas
#python classify.py -method multilabel -corpus bow_oercommons -train 14000 -test 2000 -metric cosine -destination_folder multilabel_mas






