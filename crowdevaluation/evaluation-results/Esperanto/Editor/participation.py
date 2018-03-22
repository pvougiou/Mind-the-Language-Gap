import pandas
import numpy as np

df = pandas.read_csv('processed/eo-editor.csv')

print '# participants'
print len(df.index)

print '# sentences'
sentences = len(df.columns) - 2
print len(df.columns)

print "# P all S"
print len(df.dropna().index)

print 'number participants > 50'
counter_50 = 0
for row in df.iterrows():
    rindex, dfta = row
    dfta = [x for x in dfta.tolist() if str(x) != 'nan']
    if len (dfta) >= sentences/2:
        counter_50 += 1
print counter_50

print 'Average numbers annoatated'

annotated_nr = []
for row in df.iterrows():
    rindex, dfta = row
    dfta = [x for x in dfta.tolist() if str(x) != 'nan']
    annotated_nr.append(len(dfta))
print np.mean(annotated_nr)