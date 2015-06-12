#!/usr/bin/env bash

cd ../../source

python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 5 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 10 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 20 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 50 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 100 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 200 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 500 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 1000 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 2000 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons
python classify.py -corpus bow_oer_aggregator_oercommons -corpus_training bow_oer_aggregator_oercommons -corpus_test bow_oer_aggregator_oercommons -method multilabel -cross_corpora yes -train 5000 -test 500 -metric cosine -metadata_freq 3 -destination_folder experiment_cross_corpora_train_oercommons_test_oercommons