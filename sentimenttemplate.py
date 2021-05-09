# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:28:17 2021

@author: Bichhh
"""

# Sentiment template

#%%
stopwords = open('stopwords').read().split("\n")
positive = open('positive.txt').read().split("\n")
negative = open('negative.txt').read().split("\n")

def statistics(url):
    file = open(url,"r")
    d = {}
    line = file.readline()
    while line:
        lower = line.lower()
        cleaned = re.sub('[^a-z\'\- ]','', lower)
        words = cleaned.strip().split(' ')
        for w in words:
            if w in d:
                d[w] += 1
            elif w not in stopwords:
                d[w] = 1
        line = file.readline()
    file.close()
    return d

def sentiments(url):
    d = statistics(url)
    pcount = 0
    ncount = 0
    for word in positive:
        if word in d:
            pcount = pcount + d[word]
    for word in negative:
        if word in d:
            ncount = ncount + d[word]
    return int(pcount/(pcount+ncount)*100)

def compare(url,words):
    d = statistics(url)
    counts = []
    for word in words:
        if word in d:
            counts.append(d[word])
        else:
            counts.append(0)
    # words and counts are both lists
    matplotlib.pyplot.bar(words,counts)
    
def zipfian(url):
    d = statistics(url)
    values = sorted(list(d.values()))
    values.reverse()
    matplotlib.pyplot.plot(values)
    



#%%
def load_text(path): 
    file = open(path, "r", encoding="utf8")
    lines = []
    for line in file: 
        line = line.lower()
        line = re.sub('[^a-z\'\- ]','', line).strip()
        lines.append(line)
    return lines


text = load_text("texts/nameoftext")

def context(text, word): 
    context_dictionary = {}
    for line in text: 
        if word.lower() in line.split(" "): 
            for w in line.split(" "):
                if w != word and w not in stopwords:
                    if w in context_dictionary.keys(): 
                        context_dictionary[w] += 1
                    else: 
                        context_dictionary[w] = 1 
    return context_dictionary


print(context(text, "nameoftext"))