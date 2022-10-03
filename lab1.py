import nltk
path = "dataset.txt"

from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

def graphematicAnalyze(text):
    sents=text
    result_list=[]
    stop_words=set(stopwords.words('russian'))
    for words in sents:
        words = "".join([letter for letter in words if letter not in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—»«"])
        words=word_tokenize(words)

        no_stop_word = [word.lower() for word in words if not word.lower() in stop_words]
        for word2 in no_stop_word:
            result_list.append(word2)
    wordFreq={}
    for word in result_list:
        if word in wordFreq.keys():
            wordFreq[word]+=1
        else:
            wordFreq[word]=1
    print()
    sortedList = {k: v for k, v in sorted(wordFreq.items(), key=lambda  item: (-item[1], item[0]))}

    for word in sortedList:
        print(word, sortedList[word])
    file.close()

def divideOnSentenses():
    file = open(path, "r", encoding="utf8")
    text = file.readlines()
    index = 1
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            print(str(index) + ": " + str(sentences[i]))
            index+=1
    file.close()

def divideOnWords():
    file = open(path, "r", encoding="utf8")
    text = file.readlines()
    index = 1
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            sent = sentences[i]
            words = word_tokenize(sent)
            print("Слова из предложения " + str(index) + ":", sep="")
            print(words, sep=" ")
            index += 1
    file.close()

def downLoadStopWords():
    nltk.download("punkt")
    nltk.download("stopwords")

def printStopWords():
    print("Стоп-слова:")
    print(stopwords.words('russian'))

def deleteStopWords():
    file = open(path, "r", encoding="utf8")
    text = file.readlines()
    index = 1
    st_words = set(stopwords.words('russian'))
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
             sent = sentences[i]
             words = word_tokenize(sent)
             without_stop_words = [word for word in words if not word.lower() in st_words]
             print("Слова из предложения " + str(index) + " без стоп-слов:", sep="")
             print(without_stop_words, sep=" ")
             index += 1
    file.close()

divideOnSentenses()
print()
divideOnWords()
print()
downLoadStopWords()
print()
printStopWords()
print()
deleteStopWords()
print()

file = open(path, "r", encoding="utf8")
text = file.readlines()
graphematicAnalyze(text)