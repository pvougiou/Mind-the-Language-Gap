import pandas
import numpy as np

df_q = pandas.read_csv('processed/ar-quality.csv')
df_a = pandas.read_csv('processed/ar-appropriate.csv')

df_news = df_q[[i for i in df_q.columns if 'news' in i]]
df_wiki = df_q[[i for i in df_q.columns if 'wiki' in i]]
df_ai = df_q[[i for i in df_q.columns if 'ai' in i]]

print 'Fluency'

print 'NEWS'
annotated_nr = []
for row in df_news.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
#print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))

print 'WIKI'
annotated_nr = []
for row in df_wiki.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
#print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))

print 'AI'
annotated_nr = []
for row in df_ai.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
#print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))

print 'Appriopriatenss'

df_news = df_a[[i for i in df_a.columns if 'news' in i]]
df_wiki = df_a[[i for i in df_a.columns if 'wiki' in i]]
df_ai = df_a[[i for i in df_a.columns if 'ai' in i]]

print 'NEWS'
annotated_nr = []
for row in df_news.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
#print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))

print 'WIKI'
annotated_nr = []
for row in df_wiki.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
#print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))

print 'AI'
annotated_nr = []
for row in df_ai.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
#print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))