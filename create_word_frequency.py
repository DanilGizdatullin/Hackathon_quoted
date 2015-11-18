import nltk
import pickle

from nltk.corpus import brown
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
# wordnet_lemmatizer.lemmatize

all_words_lemms = []
cnt = 0
current = 1
for cat in brown.categories():
    print(current)
    current += 1
    category_words = brown.words(categories=cat)
    all_words_lemms += [wordnet_lemmatizer.lemmatize(word.lower()) for word in category_words]
fdist = nltk.FreqDist(all_words_lemms)
pickle.dump(fdist, open('lemma_frequency/brown_fdist', 'wb'))
