#!/usr/bin/env bash
cd ../../source

#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 1 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 2 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 5 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 10 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 20 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 50 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 100 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus bow_reuters_21578 -method kneighbors -train 500 -n_neighbors 250 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard

#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 1 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 2 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 5 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 10 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 20 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 50 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 100 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
#python classify.py -corpus boc_reuters_21578 -method kneighbors -train 500 -n_neighbors 250 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard

python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 1 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 2 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 5 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 10 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 20 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 50 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 100 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard
python classify.py -corpus boc_reuters_21578_expanded -method kneighbors -train 500 -n_neighbors 250 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard -destination_folder experiment_knn_reuters_21578_wf_th_0.01_varying_n_neighbors_jaccard




