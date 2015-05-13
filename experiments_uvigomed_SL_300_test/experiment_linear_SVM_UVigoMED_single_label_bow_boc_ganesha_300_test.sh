cd ..

python classify.py -corpus bow_uvigomed -method linear_SVM  -train 5 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 10 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 15 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 20 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 25 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 30 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 40 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 50 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 75 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 100 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 150 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 300 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 500 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 750 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test
python classify.py -corpus bow_uvigomed -method linear_SVM  -train 1000 -test 300 -destination_folder linear_SVM_uvigomed_SL_SL_300_test


