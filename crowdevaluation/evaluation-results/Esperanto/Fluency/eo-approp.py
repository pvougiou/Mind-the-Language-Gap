import pandas

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def percentage(part, otherpart):
    whole = part + otherpart
    return 100 * float(part)/float(whole)

df = pandas.read_csv('processed/eo-appropriate.csv')

df_news = df[[i for i in df.columns if 'news' in i]]
df_wiki = df[[i for i in df.columns if 'wiki' in i]]
df_ai = df[[i for i in df.columns if 'ai' in i]]

df = df[[i for i in df.columns if 'news' in i or 'wiki' in i or 'ai' in i]]

all_data = {'Jes': 0, 'Ne': 0}
for column in df.columns:
    data = df[column].value_counts().to_dict()
    if 'Jes' in data:
        all_data['Jes'] += data['Jes']
    if 'Ne' in data:
        all_data['Ne'] += data['Ne']

print percentage(all_data['Jes'], all_data['Ne'])


news_data = {'Jes': 0, 'Ne': 0}
for column in df_news.columns:
    data = df_news[column].value_counts().to_dict()
    if 'Jes' in data:
        news_data['Jes'] += data['Jes']
    if 'Ne' in data:
        news_data['Ne'] += data['Ne']

news_yes = percentage(news_data['Jes'], news_data['Ne'])
news_no = percentage(news_data['Ne'], news_data['Jes'])

wiki_data = {'Jes': 0, 'Ne': 0}
for column in df_wiki.columns:
    data = df_wiki[column].value_counts().to_dict()
    if 'Jes' in data:
        wiki_data['Jes'] += data['Jes']
    if 'Ne' in data:
        wiki_data['Ne'] += data['Ne']

wiki_yes = percentage(wiki_data['Jes'], wiki_data['Ne'])
wiki_no = percentage(wiki_data['Ne'], wiki_data['Jes'])

ai_data = {'Jes': 0, 'Ne': 0}
for column in df_ai.columns:
    data = df_ai[column].value_counts().to_dict()
    if 'Jes' in data:
        ai_data['Jes'] += data['Jes']
    if 'Ne' in data:
        ai_data['Ne'] += data['Ne']

ai_yes = percentage(ai_data['Jes'], ai_data['Ne'])
ai_no = percentage(ai_data['Ne'], ai_data['Jes'])

with open('processed/eo-result-appro.csv', 'w') as outfile:
    outfile.write('news_yes\t' + 'news_no\t' + 'wiki_yes\t' + 'wiki_no\t' + 'ai_yes\t' + 'ai_no\t' + '\n')
    outfile.write(str(news_yes) + '\t' + str(news_no) + '\t' + str(wiki_yes) + '\t' + str(wiki_no) + '\t' + str(ai_yes) + '\t' + str(ai_no) + '\n')