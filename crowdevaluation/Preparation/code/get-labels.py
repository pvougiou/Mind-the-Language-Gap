import os
import io
import json
import requests

# In order to get labels from Wikidata dump run command:
# bzcat wikidata-20170418-truthy-BETA.nt.bz2 | grep -E "schema.org/name|skos/core#altLabel" | awk '{$2="";print $0}' | sed 's/\(.*\)\@/\1\t/' | sed 's/  /\t/g' | perl -pe 's/(?<!\\)"//g' | awk '{gsub(/\<|\>/,"",$1)}1' > wikidata-labels.csv
# and filter for respective language

#language code
lc = 'eo'

def getLabel(itemuri, labels):
    item = itemuri
    if 'Q' in itemuri:
        item = itemuri.replace('http://www.wikidata.org/entity/', '')
    if 'P' in itemuri:
        item = itemuri.replace('http://www.wikidata.org/prop/direct/', '')
    if item in labels:
        return labels[item]
    elif 'Q' in item and item in labels_en and item not in labels:
        return labels_en[item]
    else:
        return itemuri


def getPropLabel(prop_uris):
    result = {}
    props = '|'.join([i.replace('http://www.wikidata.org/prop/direct/', '').strip() for i in prop_uris])
    url = 'https://www.wikidata.org/w/api.php?action=wbgetentities&props=labels&languages='+lc+'&format=json&ids=' + props
    data = json.loads(requests.get(url).text)['entities']
    for key, value in data.iteritems():
        if 'labels' in data[key] and lc in data[key]['labels']:
            result[key] = value['labels'][lc]['value']
    return result


labels = {}
with io.open('wikidata-labels-'+ lc +'.csv', encoding='utf-8') as labelfile:
    for line in labelfile:
        line = line.split(' ')
        item = line[0].replace('http://www.wikidata.org/entity/', '')
        labels[item] = ' '.join(line[1:]).replace(lc + ' .', '').strip()

labels_en = {}
with io.open('wikidata-labels-en.csv', encoding='utf-8') as labelfile:
    for line in labelfile:
        line = line.split(' ')
        item = line[0].replace('http://www.wikidata.org/entity/', '')
        labels[item] = ' '.join(line[1:]).replace('en .', '').strip()

props = []
for filename in os.listdir(lc+'-triples'):
    if filename.endswith(".csv"):
        with open(lc+'-triples/' + filename) as infile:
            for line in infile:
                p = line.split('--')[1].strip()
                props.append(p)

properties = {}
chunks = [props[x:x+50] for x in xrange(0, len(props), 50)]
for c in chunks:
    properties = dict(properties.items() + getPropLabel(c).items())

for filename in os.listdir(lc + '-triples'):
    if filename.endswith(".csv"):
        with open(lc + '-triples/' + filename) as infile:
            sl = getLabel('http://www.wikidata.org/entity/' + filename.replace('-'+lc+'.csv', ''), labels).strip()
            print filename.replace('-'+lc+'.csv', '')
            for line in infile:
                tmp = line.split('--')
                p = tmp[1].strip()
                o = tmp[2].strip()
                sp = getLabel(p, properties)
                so = getLabel(o, labels)
                with io.open(lc+'-triples-labels/' + filename, 'a+', encoding='utf8') as outfile:
                    outfile.write(sl + ' -- ' + sp + ' -- ' + so + '\n')
