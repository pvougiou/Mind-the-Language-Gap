# -*- coding: utf-8 -*-

import io

#language code
lc = 'eo'

with io.open('results/'+lc+'-final-file-quality.txt', 'w', encoding='utf8') as outfile:
    with io.open('results/'+lc+'-sentences.csv', encoding='utf8') as infile:
        for line in infile:
            tmp = line.split('\t')
            with io.open(lc+'-triples-labels/' + tmp[0].replace('http://www.wikidata.org/entity/', '') + '-'+lc+'.csv', encoding='utf8') as triples:
                print tmp[1]
                outfile.write(u'<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">')
                outfile.write(tmp[1])
                outfile.write(u'</div>')
                print 'De 0 ĝis 2, ĉu la informo en la teksto kontraŭdiras la faktoj? (0 - la teksto kontraŭdiras la faktoj, 1 - la teksto enhavas pli informo ol la faktoj, 2 - la tuta informo en la teksto koncernas la faktoj, eksplicite aŭ maleksplicite).' + '\n'
                outfile.write(u'<p>De 0 ĝis 2, ĉu la informo en la teksto kontraŭdiras la faktoj? (0 - la teksto kontraŭdiras la faktoj, 1 - la teksto enhavas pli informo ol la faktoj, 2 - la tuta informo en la teksto koncernas la faktoj, eksplicite aŭ maleksplicite).</p>' + '\n')
                outfile.write(u'<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">')
                for t in triples:
                    tmp = t.split(' -- ')
                    if 'http:' not in tmp[2] and 'Point(' not in tmp[2] and 'UTC' not in tmp[2] and 'Category:' not in tmp[2]:
                        print t
                        outfile.write(t + '</br>')
                outfile.write(u'</div>')
                outfile.write(u'\n---------------------------------------------------------------\n\n')
