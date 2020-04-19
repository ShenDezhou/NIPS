# NIPS
A bigram model of titles of NIPS papers from 1987 to 2019.

# Indroduction
This project provide a method using bigrams extracted titles from NIPS accepted papers ranging from 1987 to 2019.
This simple tool use TFIDF as a ranking score in generating bigram dictionary for each bigram from title of each year's NIPS paper.
Then every bigram has a TFIDF score according to its position in every year's bigram dictionary.
The bigram score of the NIPS title corpus merges bigram files generated from each year, and add the scores if same bigram exists in two different bigram-year files.
Finally, a query tool is written using a partial matching method in bigram of the corpus, and return the matching bigram counts and get the sum of all the matching bigrams' scores.
  
# Usage
Install prerequisite dependencies `pip install falcon falcon-cors waitress`  
Serve using command: `python big_server.py`, then a backend using 8080 is started.

## Request
Request use `http://localhost:8080/bigram?q=embedding`

## Response
a dict format like
`{
   'words':[],
   'count': 0,
   'score': 0
}`
is returned.
`words` field contains all the matching bigrams, `count` field counts the matching bigrams, and `score` sums all the tfidf scores of each bigram. 
