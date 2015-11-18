import nltk
import pickle
import operator

from nltk.stem.wordnet import WordNetLemmatizer

names=set(line.strip().lower() for line in open('data/names.txt'))
fdist = pickle.load(open('lemma_frequency/brown_fdist', 'rb'))
wordnet_lemmatizer = WordNetLemmatizer()


def check_quote(quote, min_length=20, max_length=140, one_sentence=True, banned_symbols='[]@<>=', no_nnps=True):
   if len(quote) < min_length or len(quote) > max_length:
       return False
   elif any((c in set(banned_symbols)) for c in quote):
       return False
   elif no_nnps:
       text = nltk.word_tokenize(quote)
       for words in text:
           if words.lower() in names:
               return False
   return True


def sentence_complexity(sentence, fdist):
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

    word_frequency = map(lambda x: fdist[x], word_lemmatized)
    answer = {}
    for i in xrange(len(word_frequency)):
        answer[word_lemmatized[i]] = word_frequency[i]
    sorted_x = sorted(answer.items(), key=operator.itemgetter(1))
    sorted_x = list(reversed(sorted_x))

    return sorted_x

if __name__ == "__main__":
    sentence = 'Never trust a nigger: their minds and hair are full of kinks in equal measure'
    print(sentence)

    if check_quote(sentence):
        print sentence_complexity(sentence, fdist)
