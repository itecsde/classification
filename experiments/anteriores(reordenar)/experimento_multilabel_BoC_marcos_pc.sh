#!/usr/bin/env bash
python classify.py -method multilabel -corpus boc_oercommons -train 5 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 10 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 20 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 50 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 100 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 200 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 500 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 1000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 2000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 5 -test 5000 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 10 -test 5000 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 20 -test 5000 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 50 -test 5000 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 100 -test 5000 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 5000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 10000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 11000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 12000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 13000 -test 100 -metric cosine -destination_folder multilabel_BoC
python classify.py -method multilabel -corpus boc_oercommons -train 14000 -test 100 -metric cosine -destination_folder multilabel_BoC
