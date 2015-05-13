#python classify.py -corpus boc_20_newsgroup -method mbayes -train 150 -smoothing 0.001
#python classify.py -corpus boc_20_newsgroup -method mbayes -train 150 -smoothing 0.005
#python classify.py -corpus boc_20_newsgroup -method mbayes -train 150 -smoothing 0.01
#python classify.py -corpus boc_20_newsgroup -method mbayes -train 150 -smoothing 0.05
#python classify.py -corpus boc_20_newsgroup -method mbayes -train 150 -smoothing 0.1
#python classify.py -corpus boc_20_newsgroup -method mbayes -train 150 -smoothing 0.5

#python classify.py -corpus boc_ohsumed -method mbayes -train 150 -smoothing 0.001
#python classify.py -corpus boc_ohsumed -method mbayes -train 150 -smoothing 0.005
#python classify.py -corpus boc_ohsumed -method mbayes -train 150 -smoothing 0.01
#python classify.py -corpus boc_ohsumed -method mbayes -train 150 -smoothing 0.05
#python classify.py -corpus boc_ohsumed -method mbayes -train 150 -smoothing 0.1
#python classify.py -corpus boc_ohsumed -method mbayes -train 150 -smoothing 0.5

python classify.py -corpus boc_ieee -method mbayes -train 100 -test 138 -smoothing 0.001
python classify.py -corpus boc_ieee -method mbayes -train 100 -test 138 -smoothing 0.005
python classify.py -corpus boc_ieee -method mbayes -train 100 -test 138 -smoothing 0.01
python classify.py -corpus boc_ieee -method mbayes -train 100 -test 138 -smoothing 0.05
python classify.py -corpus boc_ieee -method mbayes -train 100 -test 138 -smoothing 0.1
python classify.py -corpus boc_ieee -method mbayes -train 100 -test 138 -smoothing 0.5
