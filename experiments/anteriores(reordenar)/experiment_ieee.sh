#python classify.py -corpus boc_ieee -method mbayes -train 5 -test 138
#python classify.py -corpus boc_ieee -method mbayes -train 10 -test 138
#python classify.py -corpus boc_ieee -method mbayes -train 50 -test 138

#python classify.py -corpus bow_ieee -method mbayes -train 5 -test 138
#python classify.py -corpus bow_ieee -method mbayes -train 10 -test 138
#python classify.py -corpus bow_ieee -method mbayes -train 50 -test 138

python classify.py -corpus boc_ieee_expanded -method mbayes -train 5 -test 138 -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ieee_expanded -method mbayes -train 10 -test 138 -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ieee_expanded -method mbayes -train 50 -test 138 -exp_threshold 0.8 -exp_relatedness 0.8

#python display_graphic_ieee.py experiment_ieee



