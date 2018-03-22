import io
import requests
import json
items = []

#language code
lc = 'ar'

with open('results/'+lc+'-sentences.csv') as sentences:
    for sen in sentences:
        items.append(sen.split('\t')[0].strip())
main = {}

with open('wikidata-triples.csv') as infile:
    for triple in infile:
        s = triple.split(' ')[0]
        p = triple.split(' ')[1]
        o = triple.split(' ')[2]
        triple = s + ' -- ' + p + ' -- ' + o.strip()
        if s in items:
            if s in main:
                main[s].append(triple)
            else:
                main[s] = [triple]

for item in items:
    filename = lc + '-triples/' + item.replace('http://www.wikidata.org/entity/', '') + '-'+lc+'.csv'
    with open(filename, 'w') as outfile:
        for triple in main[item]:
            print triple
            outfile.write(triple + '\n')
