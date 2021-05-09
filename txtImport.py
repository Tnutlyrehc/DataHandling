# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:06:46 2021

@author: Bichhh
"""

import re
import matplotlib

# encoding = 'utf8'

#%%

open("C:/Users/Bichhh/Desktop/SDU/Data Handling/Exam/nameoffile.txt", 'r')

#%% READ A FILE

f = open("filename.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)
f.close()    
#%% READ FILES INTO STRINGS

with open('nameoffile.txt') as f:
    lines = f.readlines()
f.close()
#%% OPEN TEXT FILE w. READ/WRITE (w+)

file_object = open("filename.txt", "w+")

#%% READ x-LINES IN TXT FILE

for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()

#%% READ LINES FROM FILE

with open("C:/Users/Bichhh/Desktop/SDU/Data Handling/Exam/nameoffile.txt") as f:
    lines = f.readlines()

count = 0
for line in lines:
    count =+1
    print(f'line {count}: {lines}')
    
    
#%%    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    