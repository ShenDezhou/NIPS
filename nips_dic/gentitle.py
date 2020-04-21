import codecs
import os

topten = ['andrew zisserman',
'bayesian networks',
'arnaud doucet',
'brain computer',
'alekh agarwal',
'alyson k. fletcher',
'bounds on',
'andrew mccallum',
'corinna cortes',
'classification with']

MODE=2

if MODE==1:
    with codecs.open('papertitle%s.utf8' %topten[0], 'w', encoding='utf-8') as fw:
        for root, dirs, files in os.walk('../acdemic_corpus/'):
            for file in files:
                print(file)
                with codecs.open(root + "/" + file, 'r', encoding='utf-8') as fd:
                    base = os.path.basename(file).split(".")[0]
                    xlines = fd.readlines()
                    assert len(xlines)>0
                    xlines = [line.strip().lower() for line in xlines]
                    print(xlines)
                    for line in xlines:
                        for bigram in topten:
                            # words = bigram.split(' ')
                            # if words[0] in line and words[1] in line:
                            if bigram in line:
                                fw.write(base+'\t'+line+'\n')
if MODE==2:
    for bigram in topten:
        with codecs.open('papertitle%s.utf8' % bigram.replace(" ",""), 'w', encoding='utf-8') as fw:
            for root, dirs, files in os.walk('../acdemic_corpus/'):
                for file in files:
                    print(file)
                    with codecs.open(root + "/" + file, 'r', encoding='utf-8') as fd:
                        base = os.path.basename(file).split(".")[0]
                        xlines = fd.readlines()
                        assert len(xlines)>0
                        xlines = [line.strip().lower() for line in xlines]
                        print(xlines)
                        for line in xlines:
                            # words = bigram.split(' ')
                            # if words[0] in line and words[1] in line:
                            if bigram in line:
                                fw.write(base+'\t'+line+'\n')
print('FIN')


