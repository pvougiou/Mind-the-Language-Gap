# -*- coding: UTF-8 -*-

import pandas
import numpy as np
from sklearn.metrics import cohen_kappa_score
from nltk import agreement

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

news = []
with open('../../../Esperanto/eo-news-sentences.csv') as infile:
    for line in infile:
        news.append(line.strip())
dbpedia = []
with open('../../../Esperanto/eo-dbpedia-sentences.csv') as infile:
    for line in infile:
        dbpedia.append(line.strip())
generated = []
with open('../../../Esperanto/eo-sentences.csv') as infile:
    for line in infile:
        generated.append(line.split('\t')[1].strip())

key_file = open('./processed/eo-fluency-keys.csv', 'w')

df = pandas.read_csv('eo-fluency.csv')
df = df.dropna(axis=1, how='all')
print 'Participants started: ' + str(len(df.index))
df = df.dropna(thresh=15)
print 'Participants counted: ' + str(len(df.index))

df_quality = df[['Participant ID']+[i for i in df.columns if '(0-6)' in i]]
df_appr = df[['Participant ID']+[i for i in df.columns if 'Could this sentence be part of Wikipedia?' in i]]

df_quality.rename(columns=lambda x: x.replace('Bonvolu taksi la tekstan kvaliton (0-6) --  -- Please evaluate the text quality (0-6)', ''), inplace=True)
df_quality.rename(columns=lambda x: x.replace('--  -- Bonvolu taksi la tekstan kvaliton (0-6) --  --  --  -- Please evaluate the text quality (0-6) --  --  --  -- ', ''), inplace=True)
df_quality.rename(columns=lambda x: x.replace(' --  --  --  -- Kiel bonskrita estas tiu frazo? --  --  --  -- How well written is this sentence? --  --  --  --', ''), inplace=True)
df_quality.rename(columns=lambda x: x.replace('--  -- Kiel bonskrita estas tiu frazo? --  -- How well written is this sentence?', ''), inplace=True)
df_quality.rename(columns=lambda x: x.strip(), inplace=True)

df_appr.rename(columns=lambda x: x.replace('Bonvolu taksi si vi pensas, ke tiu frazo povus esti frazo de Vikipedia. Ne uzu eksteran ilojn (ekzemple, Google aŭ Vikipedio) por respondi ĉi tiun demandon. --  -- Please evaluate whether you think this could be a sentence from Wikipedia. Do not use any external tools (e.g. Google or Wikipedia) to answer this question.', ''), inplace=True)
df_appr.rename(columns=lambda x: x.replace('Bonvolu taksi si vi pensas, ke tiu frazo povus esti frazo de Vikipedia. Ne uzu eksteran ilojn (ekzemple, Google aŭ Vikipedio) por respondi ĉi tiun demandon. --  --  --  -- Please evaluate whether you think this could be a sentence from Wikipedia. Do not use any external tools (e.g. Google or Wikipedia) to answer this question. --  --  --  --', ''), inplace=True)
df_appr.rename(columns=lambda x: x.replace(' --  --  --  -- Ĉu tiu frazo povus esti parto de la Vikipedio? --  --  --  -- Could this sentence be part of Wikipedia? --  --', ''), inplace=True)
df_appr.rename(columns=lambda x: x.replace('--  -- Ĉu tiu frazo povus esti parto de la Vikipedio? --  -- Could this sentence be part of Wikipedia?', ''), inplace=True)
df_appr.rename(columns=lambda x: x.strip(), inplace=True)

c = 0
for column in df_appr.columns:
    if column in news:
        df_appr.rename(columns={column: 'news_' + str(c) + '_a'}, inplace=True)
        key_file.write('news_' + str(c) + '_a' + '\t' + column + '\n')
    elif column in dbpedia:
        df_appr.rename(columns={column: 'wiki_' + str(c) + '_a'}, inplace=True)
        key_file.write('wiki_' + str(c) + '_a' + '\t' + column + '\n')
    elif column in generated:
        df_appr.rename(columns={column: 'ai_' + str(c) + '_a'}, inplace=True)
        key_file.write('ai_' + str(c) + '_a' + '\t' + column + '\n')
    c += 1

c = 0
for column in df_quality.columns:
    if column in news:
        df_quality.rename(columns={column: 'news_' + str(c) + '_q'}, inplace=True)
        key_file.write('news_' + str(c) + '_q' + '\t' + column + '\n')
    elif column in dbpedia:
        df_quality.rename(columns={column: 'wiki_' + str(c) + '_q'}, inplace=True)
        key_file.write('wiki_' + str(c) + '_q' + '\t' + column + '\n')
    elif column in generated:
        df_quality.rename(columns={column: 'ai_' + str(c) + '_q'}, inplace=True)
        key_file.write('ai_' + str(c) + '_q' + '\t' + column + '\n')
    c += 1

df_quality.to_csv('./processed/eo-quality.csv', encoding='utf-8')
df_appr.to_csv('./processed/eo-appropriate.csv', encoding='utf-8')