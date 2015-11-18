import nltk
import pickle

from nltk.corpus import brown
from nltk.stem.wordnet import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

all_words_lemms = []
cnt = 0
current = 1
for cat in brown.categories():
    print(current)
    current += 1
    category_words = brown.words(categories=cat)
    word_tags = nltk.pos_tag(category_words)

    for i in word_tags:
        if i[1][0] == 'N' or i[1][0] == 'V' or i[1][0] == 'A':
            all_words_lemms.append(wordnet_lemmatizer.lemmatize(i[0].lower(), i[1][0].lower()))
        else:
            all_words_lemms.append(wordnet_lemmatizer.lemmatize(i[0].lower()))

    # all_words_lemms += [wordnet_lemmatizer.lemmatize(word.lower()) for word in category_words]

fdist = nltk.FreqDist(all_words_lemms)
pickle.dump(fdist, open('lemma_frequency/brown_fdist', 'wb'))
