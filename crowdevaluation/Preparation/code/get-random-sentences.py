import pandas
import re
import random
import io

#language code
lc = 'ar'

data = pandas.read_csv('Arabic_LSTM_Beam_4.csv', encoding='utf-8', usecols=[0, 1])
# data['Main-Item']
# data['Summary 1']


def processing(string):
    #string = string.decode('unicode-escape')
    string = string.replace('<start>', '').replace('<end>', '')
    string = string.replace('<rare>', '(missing word)').replace('<resource>', '(missing word)')
    string = re.sub('http://www.wikidata.org/prop/direct/P[1-9]+', '(missing word)', string)
    string = string.replace('<year>', '(missing year)')
    string = string.replace(' 0 ', ' (missing value) ')
    string = string.replace('( ', '(').replace(' )', ')').replace('[ ', '[').replace(' ]', ']').replace(' :', ':')
    string = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', string)
    return string.strip()

def get_eval_sentences(sentences):
    eval_sentences = {}
    keys = sentences.keys()
    keys_random = random.sample(keys, 100)
    for key in keys_random:
        eval_sentences[data['Main-Item'][key]] = sentences[key]
    return eval_sentences

def write_to_file(sentences):
    with io.open('results/'+lc+'-sentences.csv', 'w', encoding='utf-8') as outfile:
        for item, sen in sentences.iteritems():
            outfile.write(item + '\t' + sen + '\n')

counter_clean = 0 # 169
counter_all = 0 # 288

placeholder_dict = {}
#clean_dict = {}

for key, string in data['Summary 1'].iteritems():
    arr = string.split(' ')
    c = arr.count('<rare>')
    cy = arr.count('<year>')
    cre = arr.count('<resource>')
    cp = arr.count('http://www.wikidata.org/prop/direct')
    zero = arr.count('0')
    #if c == 0 and cy == 0 and cre == 0 and zero == 0 and cp == 0:
    #    clean_dict[key] = string
    #    counter_clean += 1
    if c <= 1 and cy <= 1 and cre <= 1 and zero <= 1 and cp <= 1 and not 'interalie :' in string:
        string = processing(string)
        placeholder_dict[key] = string
        counter_all += 1
eval_sentences = get_eval_sentences(placeholder_dict)
write_to_file(eval_sentences)

#print placeholder_dict
#print counter_clean
#print counter_all
