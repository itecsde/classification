#!/usr/bin/env bash
cd ../../source

python classify.py -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
python classify.py -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_merlot -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
python classify.py -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_cnx -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh

python classify.py -corpus_training bow_oer_aggregator_merlot -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
python classify.py -corpus_training bow_oer_aggregator_merlot -corpus_test bow_oer_aggregator_merlot -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
python classify.py -corpus_training bow_oer_aggregator_merlot -corpus_test bow_oer_aggregator_cnx -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh

python classify.py -corpus_training bow_oer_aggregator_cnx -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
python classify.py -corpus_training bow_oer_aggregator_cnx -corpus_test bow_oer_aggregator_merlot -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
python classify.py -corpus_training bow_oer_aggregator_cnx -corpus_test bow_oer_aggregator_cnx -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 2 -destination_folder experiment_oer_agreggator_linear_SVC_bow_metadata_500_test.sh
