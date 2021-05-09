# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:02:55 2021

@author: Christine Line Larsen
"""
#%% 1 - Disances between Points in a 2D Space
# TASK A: Write a function distance(p,q) that returns the Euclidean distance d(p; q) between two points p and q

import math
import numpy as np 

#p = [3, 5, 2]
#q = [3, 4, 8]

#def distance(p, q):
#    distance(math.sqrt(sum[(a, b)] ** 2 for a, b in zip(p, q)))
#    return(distance)
#    print("Euclidean distance from p to q: ", distance)

from scipy.spatial import distance          

def distance(p, q):
    p, q = data[0]
    return list(map(distance.euclidean, p, q))
    
          
#%% TASK B:  Take the last digit (Z) of your exam number (DSHNVXYZ) and determine r = Z % 2.
import sklearn 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

r = 1%2
r

