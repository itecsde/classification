python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 1 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 2 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 5 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 10 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 15 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 20 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 50 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 100 -metric jaccard
python classify.py -corpus boc_ohsumed -method kneighbors -train 500 -n_neighbors 250 -metric jaccard


python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 1 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 2 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 5 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 10 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 15 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 20 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 50 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 100 -metric jaccard
python classify.py -corpus bow_ohsumed -method kneighbors -train 500 -n_neighbors 250 -metric jaccard


python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 1 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 2 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 5 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 10 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 15 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 20 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 50 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 100 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard
python classify.py -corpus boc_ohsumed_expanded -method kneighbors -train 500 -n_neighbors 250 -exp_threshold 0.8 -exp_relatedness 0.8 -metric jaccard

