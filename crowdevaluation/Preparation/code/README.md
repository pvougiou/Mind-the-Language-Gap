# Scripts to set up data for crowdevaluation

Results of the scripts in this folder, scripts in the folder c*code*

##Requirements

- wikidata-triples.csv: all triples of Wikidata from a dump in csv format 
- wikidata-labels-XX.csv: all labels for Wikidata items in a specific language in csv format
- wikidata-labels-en.csv: English labels in csv format for fallback if no label exists in specified language

##Run in the following order:

1. get-random-sentences.py
2. get-triples.py
3. get-labels.py
4. get-copy-paste.py

##Will produce the following output files (XX for the language code, in the case of Esperanto eo, for Arabic ar):

- *get-random-sentences.py*: XX-sentences.csv
- *get-triples.py*: folder (XX-triples) and file for each sentence called <entity-id>-XX.csv
- *get-labels.py*: folder (XX-triples-labels) and file for each sentence called <entity-id>-XX.csv
- *get-copy-paste.py*: a file in folder results called final-file.txt with a formatting for copy pasting the data
