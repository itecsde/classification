#!/usr/bin/env bash
python classify.py -corpus boc_ohsumed -method mbayes -train 5
python classify.py -corpus boc_ohsumed -method mbayes -train 10
python classify.py -corpus boc_ohsumed -method mbayes -train 50

python classify.py -corpus bow_ohsumed -method mbayes -train 5
python classify.py -corpus bow_ohsumed -method mbayes -train 10
python classify.py -corpus bow_ohsumed -method mbayes -train 50

python classify.py -corpus boc_ohsumed_expanded -method mbayes -train 5 -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method mbayes -train 10 -exp_threshold 0.8 -exp_relatedness 0.8
python classify.py -corpus boc_ohsumed_expanded -method mbayes -train 50 -exp_threshold 0.8 -exp_relatedness 0.8

python display_graphic_ohsumed.py experiment_ohsumed



