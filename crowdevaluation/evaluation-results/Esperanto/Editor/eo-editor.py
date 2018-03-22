# -*- coding: UTF-8 -*-

import pandas
from math import isnan
import editdistance
import numpy

key_file = open('./processed/eo-editor-keys.csv', 'w')

df = pandas.read_csv('eo-editor.csv')
df = df.dropna(axis=1, how='all')
print 'Participants started: ' + str(len(df.index))

df = df[['Participant ID']+[i for i in df.columns if 'Bonvolu skribi la unuan frazoj de Vikipedia artikilo' in i]]
df.rename(columns=lambda x: x.replace('Bonvolu skribi la unuan frazoj de Vikipedia artikilo, uzante nur la sekvantan informon:', ''), inplace=True)
df.rename(columns=lambda x: x.replace('--  --  --  --', ''), inplace=True)
df.rename(columns=lambda x: x.strip(), inplace=True)

df = df.dropna(thresh=2)
df = df.dropna(axis=1, how='all')
print 'Participants counted: ' + str(len(df.index))


c = 0
for column in df.columns:
    if not column == 'Participant ID':
        df.rename(columns={column: str(c) + '_q'}, inplace=True)
        tmp = column.split('--  --')
        sentence = tmp[0]
        triples = tmp[1:]
        key_file.write(str(c) + '_q' + '\t' + sentence + '\n')
        key_file.write(str(c) + '_q_triples' + '\t' + ';'.join(triples) + '\n')
    c += 1

df.to_csv('./processed/eo-editor.csv', encoding='utf-8')