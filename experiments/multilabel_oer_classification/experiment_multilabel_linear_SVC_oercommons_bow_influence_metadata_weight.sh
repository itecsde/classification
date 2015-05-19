#!/usr/bin/env bash
cd ..

#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 0 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 1 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 5-destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 8 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 10 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 13 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 21 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
#python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 25 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 30 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 34 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 40 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 55 -destination_folder linear_multilabel_SVC_oercommons_bow_influence_metadata_weight -algorithm linear_SVC

