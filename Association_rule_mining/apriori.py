#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 08:47:55 2019

@author: Shaikh Azamali
"""

#importing the library
import numpy as np
import matplotlib as plt
import pandas as pd

# importimg  the data set
dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
#Training apyori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003,min_confidence = 0.2, min_lift = 3, min_length = 2)

#visualizing results

results = list(rules)
results_list = []
for i in range(1,len(results)):
    results_list.append('RULE:\t' + str (results[i][0]).replace('frozenset','') +
    'n\SUPPORT:\t'+ str (results[i][1]) + 
    'n\CONF:\t' + str (results[i][2][0][2]) + 
    'n\LIFT:\t' + str (results[i][0]))

    

    
    