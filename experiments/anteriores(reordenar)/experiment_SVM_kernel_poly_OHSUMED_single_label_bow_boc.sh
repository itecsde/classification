#!/usr/bin/env bash
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 5 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 10 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 15 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 20 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 25 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 30 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 40 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 50 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 75 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 100 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel poly -train 150 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL

python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 5 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 10 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 15 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 20 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 25 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 30 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 40 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 50 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 75 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 100 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel poly -train 150 -destination_folder SVM_kernel_poly_OHSUMED_SL_kernel_poly_SL

