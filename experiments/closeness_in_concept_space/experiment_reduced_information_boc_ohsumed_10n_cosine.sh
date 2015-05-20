#!/usr/bin/env bash
cd ../../source

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 200 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 300 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 400 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine


python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 500 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 1000 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 2000 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 5000 -metric cosine -destination_folder experiment_reduced_information_boc_ohsumed_10n_cosine





