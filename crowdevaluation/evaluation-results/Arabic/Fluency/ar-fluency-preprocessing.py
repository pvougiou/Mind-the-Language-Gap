# -*- coding: UTF-8 -*-

import pandas
import numpy as np
from sklearn.metrics import cohen_kappa_score
from nltk import agreement

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

news = []
with open('../../../Arabic/ar-news-sentences.csv') as infile:
    for line in infile:
        news.append(line.strip())
dbpedia = []
with open('../../../Arabic/ar-dbpedia-sentences.csv') as infile:
    for line in infile:
        dbpedia.append(line.strip())
generated = []
with open('../../../Arabic/ar-sentences.csv') as infile:
    for line in infile:
        generated.append(line.split('\t')[1].strip())

key_file = open('./processed/ar-fluency-keys.csv', 'w')

df = pandas.read_csv('ar-fluency.csv')
df = df.dropna(axis=1, how='all')
print 'Participants started: ' + str(len(df.index))
df = df.dropna(thresh=15)
print 'Participants counted: ' + str(len(df.index))

df_quality = df[['Participant ID']+[i for i in df.columns if 'من فضلك قم بتقييم جودة النص علي مقياس من صفر 0 إلى ستة' in i]]
df_appr = df[['Participant ID']+[i for i in df.columns if 'هل تعتقد أن الجملة السابقة بإمكانها أن تستخدم كأول جملة في مقال من مقالات ويكيبيديا العربية ؟' in i]]

# Replace Quality Strings
df_quality.rename(columns=lambda x: x.replace('من فضلك قم بتقييم جودة النص علي مقياس من صفر 0 إلى ستة 6', ''), inplace=True)
df_quality.rename(columns=lambda x: x.replace('قم بتقييم جودة هذا النص:', ''), inplace=True)
df_quality.rename(columns=lambda x: x.replace('--', '').strip(), inplace=True)

#Replace Appropriateness strings
#df_appr.rename(columns=lambda x: x.replace('قيم إذا كنت تعتقد أن هذا النص من الممكن ان يكون مقتبس من ويكيبيديا العربية ام لا.', ''), inplace=True)
df_appr.rename(columns=lambda x: x.replace('--  -- قيم إذا كنت تعتقد أن هذا النص من الممكن ان يكون مقتبس من ا لويكيبيديا العربية ام لا.  --  -- لا تعتمد على أي مصادر خارجية لمعرفة الإجابة (مثل محرك بحث جوجل أو ويكيبيديا) --  --  --  --', ''), inplace=True)
df_appr.rename(columns=lambda x: x.replace('--  --  --  -- هل تعتقد أن الجملة السابقة بإمكانها أن تستخدم كأول جملة في مقال من مقالات ويكيبيديا العربية ؟', '').strip(), inplace=True)
df_appr.rename(columns=lambda x: x.replace('قيم إذا كنت تعتقد أن هذا النص من الممكن ان يكون مقتبس من ا لويكيبيديا العربية ام لا.  --  --',''), inplace=True)
df_appr.rename(columns=lambda x: x.replace('لا تعتمد على أي مصادر خارجية لمعرفة الإجابة (مثل محرك بحث جوجل أو ويكيبيديا) --  --  --  --',''), inplace=True)
df_appr.rename(columns=lambda x: x.replace('--', '').strip(), inplace=True)

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

df_quality.to_csv('./processed/ar-quality.csv', encoding='utf-8')
df_appr.to_csv('./processed/ar-appropriate.csv', encoding='utf-8')

