import os
import re


def count_words(file_cont, word):
    result = filter(lambda l: (l == word ), file_cont)
    return(len(list(result)))


#assign initial values
to_search = ["квіти", "рослини"]
files_cont = {} 
vector = []                                 
punkt = re.compile(r'\b[\w`]+\b')                 #precompilled pattern
directory = os.getcwd()                           #get current working directory
files = re.findall('text.\.txt', " ".join(sorted(os.listdir(directory))))


#indexing data
for item in files:
    freq_vector = []
    with open(directory + "/" + item, "r") as f:
        files_cont[item] = punkt.findall(f.read().lower())
        for el in to_search:
            norm_freq = 0.5 + (0.5 * (count_words(files_cont[item], el) / len(files_cont[item])))
            freq_vector.append(norm_freq)
    vector.append(freq_vector)


print(vector)
