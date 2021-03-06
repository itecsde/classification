#!/usr/bin/env bash
cd ../../source

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 0 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 10 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 20 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 30 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 40 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 50 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 60 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 70 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 80 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 90 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 100 -metric jaccard -destination_folder experiment_bow_ohsumed_varying_n_neighbors_n_features_jaccard


python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_varying_n_neighbors_n_features_jaccard



python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 0 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 10 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 20 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 30 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 40 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 50 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 60 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 70 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 80 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 90 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -kbest 100 -metric jaccard -destination_folder experiment_boc_ohsumed_expanded_varying_n_neighbors_n_features_jaccard -exp_threshold 0.8 -exp_relatedness 0.8

