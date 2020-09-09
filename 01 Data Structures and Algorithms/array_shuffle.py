#! /home/mhb/anaconda2/bin/python

import numpy as np

# create an array of values
myarr = range(1,100)
print "-" * 60
print myarr

# shuffle the values
print "-" * 60
np.random.shuffle(myarr)
print myarr
