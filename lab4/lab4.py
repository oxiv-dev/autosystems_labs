import re
import pandas as pd
import os
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt


#assign initial values
all = []                                      #all words from files
p = re.compile(r'\b[\w`]+\b')                 #precompilled pattern
directory = os.getcwd()                       #get current working directory
files = re.findall('text.\.txt', " ".join(sorted(os.listdir(directory))))


#parse data
for file in files:
    with open(directory + "/" + file, "r") as f:
        cont = p.findall(f.read().lower())
        all += cont


#cleaning data
for el in all:
    el = "".join(re.findall('\w', el))
text = " ".join(all)


#processing
tokens = word_tokenize(text)
text = nltk.text.Text(tokens)

freq = FreqDist(text)
freq_sorted = dict(sorted(freq.items(), key=lambda item: item[1]))

with open("dict_sorted.txt", "w") as f:
    for key, value in freq_sorted.items():
        f.write("{}: {}\n".format(key, value))
    f.close()

stop_words = list(filter(lambda x:(len(x) < 4), all))
stop_words = pd.unique(stop_words)

with open("stop.txt", "w") as f:
    for value in stop_words:
        f.write("{}: {}\n".format(value, all.count(value)))
    f.close()

all = list(filter(lambda x: (x not in stop_words), all))

text = " ".join(all)
tokens = word_tokenize(text)
text = nltk.text.Text(tokens)
clean_freq = FreqDist(text)

with open("clean.txt", "w") as f:
    for key, value in clean_freq.items():
        f.write("{}: {}\n".format(key, value))
    f.close()


#visualizing    
x = [el[0] for el in clean_freq.most_common(30)]
y = [el[1] for el in clean_freq.most_common(30)]
#plt.figure(num=None, figsize=(7, 6), dpi=120, facecolor='w', edgecolor='k')
plt.bar(x, y)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
