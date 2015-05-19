python classify.py -corpus boc_20_newsgroup -method mbayes -train 5
python classify.py -corpus boc_20_newsgroup -method mbayes -train 10
python classify.py -corpus boc_20_newsgroup -method mbayes -train 50

python classify.py -corpus bow_20_newsgroup -method mbayes -train 5
python classify.py -corpus bow_20_newsgroup -method mbayes -train 10
python classify.py -corpus bow_20_newsgroup -method mbayes -train 50

python classify.py -corpus boc_20_newsgroup_expanded -method mbayes -train 5 -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_20_newsgroup_expanded -method mbayes -train 10 -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_20_newsgroup_expanded -method mbayes -train 50 -exp_threshold 0.8 -exp_relatedness 0.8

python display_graphic_20_newsgroups.py experiment_1



