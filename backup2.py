from nltk import *
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import GaussianNB

jawa = []
sunda = []
indonesia = []
X = []
y = []


with open('jawa.txt', 'rt') as jw:
    for line in jw:
        jawa.append(jw.readline().split('/'))

with open('sunda.txt', 'rt') as sd:
    for line in sd:
        sunda.append(sd.readline().split('/'))

with open('indonesia.txt', 'rt') as id:
    for line in id:
        indonesia.append(id.readline().split('/'))

tweets = []
for line in jawa + sunda + indonesia:
    if(len(line) == 2):
        words = line[0]
        etnik = line[1].replace("\n","")
        words_filtered = words.split()
        tweets.append((words_filtered, etnik))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, etnik) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

all_words = get_words_in_tweets(tweets)
word_features = get_word_features(all_words)

for la in tweets:
    print(la)

# extraxted =  extract_features(word_feature)

# print(tweets)

# vectorizer = CountVectorizer()

# data_matrix = vectorizer.fit_transform(tweets)
#
# transformer = TfidfTransformer(smooth_idf=True)
#
# tfidf_feature = transformer.fit_transform(data_matrix)
#
# clf = GaussianNB()
#
# print(clf.fit(tfidf_feature.toarray(), y))

# print(tfidf_feature)



#
# training_set = classify.apply_features(tfidf_feature, tweets)
# print(training_set)

# classifier = NaiveBayesClassifier.train(training_set)
#
# def choose_class(text):
#     return classifier.classify(transformer.fit_transform(text.split()))

