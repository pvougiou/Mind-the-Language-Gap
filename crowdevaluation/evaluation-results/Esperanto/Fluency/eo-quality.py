import pandas
import operator

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_csv('processed/eo-quality.csv')
#TODO: drop only removes header, so slicing ([:1]) hack later on
df = df.drop(['Participant ID'], axis=1)

df_news = df[[i for i in df.columns if 'news' in i]]
df_wiki = df[[i for i in df.columns if 'wiki' in i]]
df_ai = df[[i for i in df.columns if 'ai' in i]]

mean_news = df_news.dropna(how='all').stack().mean()#df_news.mean().tolist()
mean_wiki = df_wiki.dropna(how='all').stack().mean()#df_wiki.mean().tolist()
mean_ai = df_ai.dropna(how='all').stack().mean()#df_ai.mean().tolist()

df = df[[i for i in df.columns if 'news' in i or 'wiki' in i or 'ai' in i]]

mean_arr = []
for column in df.columns:
    print column
    mean_arr.append(np.mean(df[column]))

print('All Mean Quality: ' + str(np.mean(mean_arr)))
print('All Std Triples: ' + str(np.std(mean_arr)))


mean_arr = []
for column in df_news.columns:
    mean_arr.append(np.mean(df_news[column]))

print('News Mean Quality: ' + str(np.mean(mean_arr)))
print('News Std Triples: ' + str(np.std(mean_arr)))

mean_arr = []
for column in df_wiki.columns:
    mean_arr.append(np.mean(df_wiki[column]))

print('Wiki Mean Quality: ' + str(np.mean(mean_arr)))
print('Wiki Std Triples: ' + str(np.std(mean_arr)))

mean_arr = []
for column in df_ai.columns:
    mean_arr.append(np.mean(df_ai[column]))

print('AI Mean Quality: ' + str(np.mean(mean_arr)))
print('AI Std Triples: ' + str(np.std(mean_arr)))


participation_news = df_news.count().tolist()
participation_wiki = df_wiki.count().tolist()
participation_ai = df_ai.count().tolist()
#means = df.mean(axis=0).tolist()[1:]
#participation = df.count().tolist()[1:]


with open('processed/eo-result-quality.csv', 'w') as outfile:
    outfile.write('news_mean\t' + 'wiki_mean\t' + 'ai_mean\t' + '\n')
    outfile.write(str(mean_news) + '\t' + str(mean_wiki) + '\t' + str(mean_ai))

with open('processed/eo-fluency-keys.csv') as inf:
    with open('../../numbers/eo-fluency-quality.txt', 'w') as out:
        news = []
        wiki = []
        ai = []
        for line in inf:
            key, value = line.split('\t')
            if 'news' in key:
                news.append(len(value.split(' ')))
            if 'wiki' in key:
                wiki.append(len(value.split(' ')))
            if 'ai' in key:
                ai.append(len(value.split(' ')))
        out.write('Mean Sentence Length News: ' + str(np.mean(news)) + '\n')
        out.write('Mean Sentence Length Wiki: ' + str(np.mean(wiki)) + '\n')
        out.write('Mean Sentence Length AI: ' + str(np.mean(ai)) + '\n')