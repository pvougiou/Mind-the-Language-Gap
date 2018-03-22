import pandas
import numpy as np

df_q = pandas.read_csv('processed/eo-quality.csv')
df_a = pandas.read_csv('processed/eo-appropriate.csv')

df_q = df_q[[i for i in df_q.columns if 'news' in i or 'wiki' in i or 'ai' in i]]
df_a = df_a[[i for i in df_a.columns if 'news' in i or 'wiki' in i or 'ai' in i]]

print '# participants'
print len(df_q.index)
print len(df_a.index)

print '# sentences'
sentences = len(df_q.columns) - 2
print len(df_q.columns)
print len(df_a.columns)

print "# P all S"
print len(df_q.dropna().index)
print len(df_a.dropna().index)

print 'number participants > 50'
counter_50 = 0
for row in df_q.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    if len (data) >= sentences/2:
        counter_50 += 1
print counter_50

counter_50 = 0
for row in df_a.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    if len (data) >= sentences/2:
        counter_50 += 1
print counter_50

print 'Average numbers annoatated'

annotated_nr = []
for row in df_q.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))

annotated_nr = []
for row in df_a.iterrows():
    rindex, data = row
    data = [x for x in data.tolist() if str(x) != 'nan']
    annotated_nr.append(len(data))
print np.mean(annotated_nr)
print 'total annotations: ' + str(sum(annotated_nr))