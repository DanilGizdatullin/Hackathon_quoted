import pickle
import nltk
import operator

from nltk.stem.wordnet import WordNetLemmatizer

fdist = pickle.load(open('lemma_frequency/brown_fdist', 'rb'))

wordnet_lemmatizer = WordNetLemmatizer()

# with open('data/quotes.txt', 'r') as myfile:
#     data = myfile.read()
# sentences = data.split('####')
# sentences = map(lambda x: x[0: -1], sentences)
# sentence = sentences[2]
sentence = 'Never trust a nigger: their minds and hair are full of kinks in equal measure'

word_tokenized = nltk.word_tokenize(sentence)
word_tokenized_filtered = []

for i in word_tokenized:
    if not('\'' in i) and not(',' in i) and not('.' in i) and not('?' in i) and not('!' in i) and not(':' in i):
        word_tokenized_filtered.append(i)
print(word_tokenized_filtered)
word_tags = nltk.pos_tag(word_tokenized_filtered)
# word_lemmatized = map(lambda x: wordnet_lemmatizer.lemmatize(x.lower()), word_tokenized_filtered)
word_lemmatized = []

for i in word_tags:
    if i[1][0] == 'N' or i[1][0] == 'V' or i[1][0] == 'A':
        word_lemmatized.append(wordnet_lemmatizer.lemmatize(i[0].lower(), i[1][0].lower()))
    else:
        word_lemmatized.append(wordnet_lemmatizer.lemmatize(i[0].lower()))
print(word_lemmatized)

word_frequency = map(lambda x: fdist[x], word_lemmatized)
answer = {}
for i in xrange(len(word_frequency)):
    answer[word_lemmatized[i]] = word_frequency[i]
sorted_x = sorted(answer.items(), key=operator.itemgetter(1))
sorted_x = list(reversed(sorted_x))
print(sentence)
# print(word_lemmatized)
# print(word_frequency)
print(sorted_x)


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

print(1)
print(sentence_complexity(sentence, fdist))
