#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:15:57 2024

@author: lizzithompson
"""

import pandas as pd

import sys
print(sys.version)
import sklearn
from sklearn import linear_model

analysis_data = pd.read_csv("analysis_data_small.csv").values

print(analysis_data)