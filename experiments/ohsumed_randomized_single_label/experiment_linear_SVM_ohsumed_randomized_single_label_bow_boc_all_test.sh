#!/usr/bin/env bash
cd ../../source

python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 5  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 10  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 15  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 20  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 25  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 30  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 40  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 50  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 75  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 100  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 150  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 300  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 500  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 750  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus boc_ohsumed_randomized -method linear_SVM  -train 1000  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test

python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 5  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 10  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 15  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 20  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 25  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 30  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 40  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 50  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 75  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 100  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 150  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 300  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 500  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 750  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
python classify.py -corpus bow_ohsumed_randomized -method linear_SVM  -train 1000  -destination_folder linear_SVM_ohsumed_randomized_SL_SL_all_test
