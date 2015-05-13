
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 100 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 200 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 300 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 400 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev

python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 500 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 1000 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 2000 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -kbest 5000 -metric chebyshev -destination_folder experiment_reduced_information_boc_ohsumed_10n_chebyshev



