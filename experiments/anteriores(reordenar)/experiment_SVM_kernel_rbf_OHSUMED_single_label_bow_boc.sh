#!/usr/bin/env bash
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 5 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 10 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 15 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 20 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 25 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 30 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 40 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 50 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 75 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 100 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel rbf -train 150 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL

python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 5 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 10 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 15 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 20 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 25 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 30 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 40 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 50 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 75 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 100 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel rbf -train 150 -destination_folder SVM_kernel_rbf_OHSUMED_SL_kernel_rbf_SL

