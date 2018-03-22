# -*- coding: UTF-8 -*-

import pandas
from math import isnan
import editdistance
import numpy

key_file = open('./processed/ar-editor-keys.csv', 'w')

df = pandas.read_csv('ar-editor.csv')
df = df.dropna(axis=1, how='all')
print 'Participants started: ' + str(len(df.index))

df = df[['Participant ID']+[i for i in df.columns if 'من فضلك قم بكتابة فقرة من الممكن أن تستخدم كأول فقرة في صفحة الويكيبيديا' in i]]
df.rename(columns=lambda x: x.replace('من فضلك قم بكتابة فقرة من الممكن أن تستخدم كأول فقرة في صفحة الويكيبيديا الخاصة بهذا الموضوع باستخدام المعلومات المعطاة لك فقط.', ''), inplace=True)
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

df.to_csv('./processed/ar-editor.csv', encoding='utf-8')