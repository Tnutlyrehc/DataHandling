# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:34:30 2021

@author: Bichhh
"""

import json 


#%% DESERIALISED EXAMPLE
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)



#%%

f = open('nameofdocument.json')
data = json.load(f)

for i in data['emp_details']:
    print(i)

f.close()


#%% JSON TO ARRAY

import json

input_file = open ('stores-small.json')
json_array = json.load(input_file)
store_list = []

for item in json_array:
    store_details = {"name":None, "city":None}
    store_details['name'] = item['name']
    store_details['city'] = item['city']
    store_list.append(store_details)

print(store_list)