#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 1
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 2
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 5
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 10
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 20
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 50
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 100
#python classify.py -corpus boc_20_newsgroup -method kneighbors -train 500 -n_neighbors 250

#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 1
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 2
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 5
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 10
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 20
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 50
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 100
#python classify.py -corpus bow_20_newsgroup -method kneighbors -train 500 -n_neighbors 250


python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 1 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 2 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 5 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 10 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 20 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 50 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 100 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine
python classify.py -corpus boc_20_newsgroup_expanded -method kneighbors -train 500 -n_neighbors 250 -exp_threshold 0.8 -exp_relatedness 0.8 -metric cosine -destination_folder experiment_knn_20ng_wf_th_0.01_varying_n_neighbors_cosine




