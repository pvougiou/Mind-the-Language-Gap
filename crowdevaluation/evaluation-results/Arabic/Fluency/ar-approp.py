# -*- coding: UTF-8 -*-

import pandas

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from nltk import agreement
import math


def percentage(part, otherpart):
    whole = part + otherpart
    if not whole == 0:
        return 100 * float(part)/float(whole)
    else:
        return 0

df = pandas.read_csv('processed/ar-appropriate.csv')

df_news = df[[i for i in df.columns if 'news' in i]]
df_wiki = df[[i for i in df.columns if 'wiki' in i]]
df_ai = df[[i for i in df.columns if 'ai' in i]]

df = df[[i for i in df.columns if 'news' in i or 'wiki' in i or 'ai' in i]]

all_data = {'نعم': 0, 'لا': 0}
for column in df.columns:
    data = {}
    for k, v in df[column].value_counts().to_dict().iteritems():
        data[k.strip()] = v
    if 'نعم' in data:
        all_data['نعم'] += data['نعم']
    if 'لا' in data:
        all_data['لا'] += data['لا']

print percentage(all_data['نعم'], all_data['لا'])

news_data = {'نعم': 0, 'لا': 0}
for column in df_news.columns:
    data = {}
    for k, v in df_news[column].value_counts().to_dict().iteritems():
        data[k.strip()] = v
    if 'نعم' in data:
        news_data['نعم'] += data['نعم']
    if 'لا' in data:
        news_data['لا'] += data['لا']

news_yes = percentage(news_data['نعم'], news_data['لا'])
news_no = percentage(news_data['لا'], news_data['نعم'])

wiki_data = {'نعم': 0, 'لا': 0}
for column in df_wiki.columns:
    data = {}
    for k, v in df_wiki[column].value_counts().to_dict().iteritems():
        data[k.strip()] = v
    if 'نعم' in data:
        wiki_data['نعم'] += data['نعم']
    if 'لا' in data:
        wiki_data['لا'] += data['لا']

wiki_yes = percentage(wiki_data['نعم'], wiki_data['لا'])
wiki_no = percentage(wiki_data['لا'], wiki_data['نعم'])

ai_data = {'نعم': 0, 'لا': 0}
for column in df_ai.columns:
    data = {}
    for k, v in df_ai[column].value_counts().to_dict().iteritems():
        data[k.strip()] = v
    if 'نعم' in data:
        ai_data['نعم'] += data['نعم']
    if 'لا' in data:
        ai_data['لا'] += data['لا']

ai_yes = percentage(ai_data['نعم'], ai_data['لا'])
ai_no = percentage(ai_data['لا'], ai_data['نعم'])


with open('processed/ar-result-appro.csv', 'w') as outfile:
    outfile.write('news_yes\t' + 'news_no\t' + 'wiki_yes\t' + 'wiki_no\t' + 'ai_yes\t' + 'ai_no\t' + '\n')
    outfile.write(str(news_yes) + '\t' + str(news_no) + '\t' + str(wiki_yes) + '\t' + str(wiki_no) + '\t' + str(ai_yes) + '\t' + str(ai_no) + '\n')