#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import pickle
import operator

from nltk.stem.wordnet import WordNetLemmatizer

names=set(line.strip().lower() for line in open('data/names.txt'))
fdist = pickle.load(open('lemma_frequency/brown_fdist', 'rb'))
wordnet_lemmatizer = WordNetLemmatizer()


def check_quote(quote, min_length=20, max_length=140, one_sentence=True, banned_symbols='[]@<>=', no_nnps=True):
   if len(quote) < min_length or len(quote) > max_length:
       # print 'Wrong len'
       return False
   elif any((c in set(banned_symbols)) for c in quote):
       # print 'Bad symbol'
       return False
   elif no_nnps:
       text = nltk.word_tokenize(quote)
       for words in text:
           if words.lower() in names:
               # print 'Name in quote'
               return False
   return True


def sentence_complexity(sentence, frequency_dist=fdist):
    word_tokenized = nltk.word_tokenize(sentence)
    word_tokenized_filtered = []
    for i in word_tokenized:
        if not('\'' in i) and not(',' in i) and not('.' in i) and not('?' in i) and not('!' in i) and not(':' in i):
            word_tokenized_filtered.append(i)

    word_tags = nltk.pos_tag(word_tokenized_filtered)
    word_lemmatized = []
    for i in word_tags:
        if i[1][0] == 'N' or i[1][0] == 'V' or i[1][0] == 'A':
            word_lemmatized.append(wordnet_lemmatizer.lemmatize(i[0].lower(), i[1][0].lower()))
        else:
            word_lemmatized.append(wordnet_lemmatizer.lemmatize(i[0].lower()))

    word_frequency = map(lambda x: frequency_dist[x], word_lemmatized)
    word_frequency.sort()
    # print(word_frequency[0:3])
    complexity = 1 / float(sum(word_frequency[0:3]))
    # answer = {}
    # for i in xrange(len(word_frequency)):
    #     answer[word_lemmatized[i]] = word_frequency[i]
    # sorted_x = sorted(answer.items(), key=operator.itemgetter(1))
    # sorted_x = list(reversed(sorted_x))

    return complexity

if __name__ == "__main__":
    sentence = [0, 0, 0, 0, 0]
    sentence[0] = 'Never trust a nigger: their minds and hair are full of kinks in equal measure'
    sentence[1] = 'I am Beloved and she is mine. I see her take flowers away from leaves.'
    sentence[2] = 'A man of genius makes no mistakes. His errors are volitional and are the portals of discovery'
    sentence[3] = 'Of children as of procreation the pleasure momentary, the posture ridiculous, the expense damnable.'
    sentence[4] = 'The most bitter insult one can offer to a Londoner is ""bastard"" — which", taken for what it means," is hardly an insult at all.'
    for i in xrange(5):
        if check_quote(sentence[i]):
            print(sentence_complexity(sentence[i], fdist))
