#!/usr/bin/env bash
cd ../../source

python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 200 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 300 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 400 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan


#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 500 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan
#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 1000 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan
#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 2000 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan
#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 5000 -metric manhattan -destination_folder experiment_reduced_information_bow_ohsumed_10n_manhattan


