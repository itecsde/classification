#!/usr/bin/env bash
cd ..

python classify.py -corpus bow_oercommons -method multilabel -train 5 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 10 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 20 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 50 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 100 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 200 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 500 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 1000 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 2000 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
python classify.py -corpus bow_oercommons -method multilabel -train 5000 -test 500 -metric cosine -metadata_freq 3 -destination_folder linear_multilabel_SVC_oercommons_multilabel_bow_metadata_freq_3 -algorithm linear_SVC
