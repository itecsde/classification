#!/usr/bin/env bash
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 5 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 10 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 15 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 20 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 25 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 30 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 40 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 50 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 75 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 100 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus bow_ohsumed -method SVM -kernel sigmoid -train 150 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL

python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 5 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 10 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 15 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 20 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 25 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 30 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 40 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 50 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 75 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 100 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL
python classify.py -corpus boc_ohsumed -method SVM -kernel sigmoid -train 150 -destination_folder SVM_kernel_sigmoid_OHSUMED_SL_kernel_sigmoid_SL

