
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 200 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 300 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 400 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean

#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 500 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean
#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 1000 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean
#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 2000 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean
#python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 5000 -metric euclidean -destination_folder experiment_reduced_information_bow_ohsumed_10n_euclidean


