cd ..
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 5 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 10 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 20 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 50 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 100 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 200 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 500 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 1000 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 2000 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test
python classify.py -corpus_training boc_reuters_rcv1 -corpus_test boc_reuters_rcv2 -method cross_language_linear_SVM -train 5000 -test 2000 -metric cosine -destination_folder train_rcv1_test_rcv2_2000_test

