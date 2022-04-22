import re
import pandas as pd
import os
import locale

locale.setlocale(category=locale.LC_ALL, locale='uk_UA')


def count_words(file_cont, n):
    result = filter(lambda l: (len(l) == n), file_cont)
    return(len(list(result)))


#assign initial values
files_cont = {}                                   #content of each file(dict "filename":"string")
files_dict = {}                                   #dict for each file
all = []                                          #all content from files
punkt = re.compile(r'\b[\w`]+\b')                 #precompilled pattern
directory = os.getcwd()                           #get current working directory
files = re.findall('text.\.txt', " ".join(sorted(os.listdir(directory))))


#collecting data
for item in files:
    f = open(directory + "/" + item, "r")
    words = punkt.findall(f.read().lower())
    all += words
    files_cont[item] = " ".join(words)
    for el in pd.unique(words):
        try:
            files_dict[item][el] = words.count(el)
        except:
            files_dict[item] = {}
            files_dict[item][el] = words.count(el)

#write to file
all = sorted(all, key=locale.strxfrm)
f = open("dictionary.txt", "w")
f.write(" ".join(pd.unique(all)))
f.close()

#write to csv
final = pd.DataFrame(columns = files, index = pd.unique(all))

for index, row in final.iterrows():
    for name in files:
        try:
            row[name] = files_dict[name][index]
        except:
            row[name] = 0

final.to_csv("total.csv")


#variant
n = int(input("Enter n: "))
dict_num = {}
for item in files:
    l = files_cont[item].split(" ")
    dict_num[item] = count_words(l, n)

for key, value in dict_num.items():
    print("{}: {}".format(key, value))


