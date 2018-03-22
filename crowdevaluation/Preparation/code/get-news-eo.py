#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In the current setup, it's 94 sentences from eo news

import random
import requests
from lxml import html
import io

def make_sentence(abstract):
    sentence = abstract.split('.')[0]
    return sentence + '.'

sentences = []
counter_missing = 0

random_numbers = random.sample(range(1000, 2000), 100)

with io.open('results/eo-news-sentences.csv', 'w', encoding='utf-8') as outfile:
    for n in random_numbers:
        print n
        url = 'http://eo.mondediplo.com/article' + str(n) + '.html'
        site = requests.get(url)
        #print site.text
        tree = html.fromstring(site.content)
        xpath_query = "//p"
        query_results = tree.xpath(xpath_query)
        sentence = query_results[0].text_content().encode('utf-8')
        if not sentence:
            if len(query_results) > 1:
                sentence = query_results[1].text_content().encode('utf-8')
            else:
                print 'missing sentence'
                counter_missing += 1
                continue
        sentence = make_sentence(sentence)
        if 'The requested URL' in sentence:
            counter_missing += 1re
            continue
        print sentence
        outfile.write(sentence.decode('utf-8') + '\n'.decode('utf-8'))
        print '------------------------------------'

print counter_missing