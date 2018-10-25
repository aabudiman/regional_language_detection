import pandas as pd

df = pd.read_excel('dataset.xlsx')

# print(df.word)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))

features = tfidf.fit_transform(df.word).toarray()
labels = df.label
features.shape

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy

from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
import get_data

numpy.set_printoptions(threshold=numpy.nan)

X_train, X_test, y_train, y_test = train_test_split(df['word'], df['label'], test_size=0.333, shuffle=True)
count_vect = CountVectorizer(ngram_range=(1, 2))
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

# print (count_vect.transform(X_test).toarray())

# print (X_train_tfidf.toarray())


# tebak = clf.predict(count_vect.transform(X_test))
#
# # print (tebak);

def tebak(kalimat):
    hasil = clf.predict(count_vect.transform([kalimat]))
    return hasil

def tebakAkun(akun):
    import get_data
    datas  = get_data.getData(akun)
    for data in datas:
        print(data.text)
        tebak(data)

def uji2(xtrain,y):
    prediksi = []
    for x in xtrain:
        prediksi.append(tebak(x))
    acc = accuracy_score(y,prediksi)
    prc = precision_score(y, prediksi, average='micro')
    rcl = recall_score(y, prediksi, average='micro')
    cnf = confusion_matrix(y, prediksi, labels=["jawa", "sunda", "indonesia"])

    print("Accuracu: ",acc)
    print("Precision: ",prc)
    print("Recall: ",rcl)
    print("Confusion Matrix: ")
    print(cnf)

uji2(X_train,y_train)


akun = input("Masukkan nama akun (tanpa @):")
datas = get_data.getData(akun)
for data in datas:
    if(data.text != ''):
        print(data.text)
        print(tebak(data.text))

#
# i=0
# benar = 0
# salah = 0
# for ln in y_test:
#     if(ln == tebak[i]):
#         benar += 1
#     else:
#         salah += 1
#     # print (ln +"  "+tebak[i])
#     print("bahasa sebenarnya adalah ",ln," diprediksi sebagai ",tebak[i])
#     i += 1
# print("benar: ", (benar))
# print("salah: ", (salah))

#
#
# models = [
#     MultinomialNB(),
# ]
#
#
#
#
# def uji():
#     CV = 10
#     cv_df = pd.DataFrame(index=range(CV * len(models)))
#     entries = []
#     pre = []
#     rec = []
#     dataa = tfidf_transformer.fit_transform(count_vect.fit_transform(df['word']))
#     for model in models:
#       model_name = model.__class__.__name__
#       accuracies = cross_val_score(model, features, labels, cv=CV)
#       # print(accuracies, model_name)
#       fitt =  model.fit(dataa,labels)
#       pred = fitt.predict(dataa)
#       # precision_recall = classification_report(labels, pred)
#       precision = precision_score(labels, pred, average='micro')
#       pre.append(precision)
#       recall =  recall_score(labels, pred, average='micro')
#       rec.append(recall)
#       tn = confusion_matrix(labels, pred, labels=["jawa", "sunda", "indonesia"])
#       for fold_idx, accuracy in enumerate(accuracies):
#         entries.append((model_name, fold_idx, accuracy))
#     cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
#     #
#     pre.sort()
#     print(cv_df.groupby('model_name').accuracy.mean())
#     print("precision",pre )
#     print("recall",rec)
#     print("Confused matrix")
#     print(tn)
    # print("FP",fp)
    # print("FN",fn)
    # print("TP",tp)

# kalimat = input("masukkan kalimat:")

# def testFromAccount(akun):
#     datas = get_data.getData(akun)
#     for data in datas:
#         tebak(data.text)
# tebak("semua keinginan pacar diturutin keinginan orang tua didenger aja ngga mau jadi apa anak muda jaman sekarang")
# uji()
# testFromAccount("thekakek")

