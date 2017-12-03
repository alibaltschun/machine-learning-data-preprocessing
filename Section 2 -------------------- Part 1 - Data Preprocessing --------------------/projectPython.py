# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:04:26 2017

@author: Ali Baltschun
"""

# Data Processing

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values