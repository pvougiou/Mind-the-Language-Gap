#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import io

data = []

def make_sentence(abstract):
    sentence = abstract.split('.')[0]
    return sentence + '.'

with open('dbpedia-abstracts-eo.csv') as infile:
    for line in infile:
        sentence = line.split('\t')[1]
        if not 'interalie:' in sentence:
            data.append(sentence.decode('utf-8'))

with io.open('eo-dpedia-sentences.csv', 'w', encoding='utf-8') as outfile:
    for abstract in random.sample(data, 100):
        outfile.write(make_sentence(abstract) + '\n')