import numpy as np
import pandas as pd
import nltk

word_dictionary = []

dataset = pd.read_csv('fake reviews dataset.csv')
for review in dataset['text_']:
    token = nltk.word_tokenize(review)
    for word in token:
        if word not in word_dictionary:
            word_dictionary.append(word)
print(word_dictionary)
