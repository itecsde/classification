cd ..

python classify.py -corpus bow_uvigomed -method linear_SVM -train 5 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat
python classify.py -corpus bow_uvigomed -method linear_SVM -train 10 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 20 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 50 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 100 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 200 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 500 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 1000 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 2000 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
python classify.py -corpus bow_uvigomed -method linear_SVM -train 5000 -test 1000 -metric cosine -destination_folder linear_SVC_uvigomed_5000_1000_aleat 
