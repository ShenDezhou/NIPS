import os

from sklearn.feature_extraction.text import TfidfVectorizer
import codecs
import numpy
#from nltk.stem.snowball import SnowballStemmer

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default='../acdemic_corpus/pytorch.txt', help='input file')
args = parser.parse_known_args()[0]

base = os.path.basename(args.file).split(".")[0]


class StemmedTfidfVectorizer(TfidfVectorizer):

    def __init__(self, stemmer, *args, **kwargs):
        super(StemmedTfidfVectorizer, self).__init__(*args, **kwargs)
        self.stemmer = stemmer

    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda doc: (self.stemmer.stem(word) for word in analyzer(doc.replace('\n', ' ')))

with codecs.open(args.file,'r', encoding='utf-8') as fd:
    with codecs.open(base+'bigram.utf8', 'w', encoding='utf-8') as fb:
        xlines = fd.readlines()
        xlines = [line.strip() for line in xlines if len(line.strip())>10]

        # stemmer = SnowballStemmer('english', ignore_stopwords=False)
        vectorizer = TfidfVectorizer(
                                    # stemmer=stemmer,
                                    analyzer= 'word',
                                    lowercase=True,
                                    ngram_range=(2,2),
                                    max_features =None,
                                )

        X = numpy.array(xlines)
        vectorizer.fit_transform(X)
        dic =vectorizer.vocabulary_
        dic =sorted(dic.items(), key=lambda d: int(d[1]), reverse=True)
        voc = [i[0] for i in dic]
        print(len(voc), voc)
        for w in voc:
            fb.write(w+'\n')

print('FIN')
