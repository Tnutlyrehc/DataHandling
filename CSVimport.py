# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:32:28 2021

@author: Bichhh
"""
#%% READ 

import csv

with open(' .txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} text text text {row[1] text, and text {row[2]}.')
            line_count() += 1
    print(f'Processed{line_count} lines.')
    

#%% IMPORT CSV FILE WITH CSV.READER()

import csv

with open('nameoffile.csv', 'r') as file: 
    reader = csv.reader(file)
    for row in reader: 
        print(row)
        
        
#%% IMPORT CSV FILE HAVING TAB DELIMITER  

with open('nameoffile.csv', 'r' as file):
    reader = csv.reader(file, delimiter = '\t')
    for row in reader: 
        print(row)
        
#%% IMPORT CSV FILE WITH INITIAL SPACES 

import csv
with open('nameoffile.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)
        
#%% IMPORT CSV FILE WITH QUOTES 

import csv
with open('nameoffile.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)
        

#%% IMPORT CSV FILE WITH DICTREADER
        
import csv
with open("nameoffile.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))        

#%% IMPORT USING CSV.SNIFFER() TO DEDUCE THE DIALECT OF CSV FILE

import csv
with open('nameoffile.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)

    deduced_dialect = csv.Sniffer().sniff(sample)

with open('nameoffile.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)

    for row in reader:
        print(row)


#%% PRINT A SPECIFIC ROW FROM THE READER 
for row in reader:
        content = list(row[i] for i in included_cols)
        print content

#WITH PANDAS 
import pandas as pd
df = pd.read_csv(csv_file)
saved_column = df.column_name

#%% IMPORT CSV AND SELECT COLUMNS 

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('file.txt') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(columns['name'])
print(columns['phone'])
print(columns['street'])






















