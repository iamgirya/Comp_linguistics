from nltk import sent_tokenize
from nltk import word_tokenize
from pymorphy2 import MorphAnalyzer

def getWordsListFromText(text):
    words = []
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            sent = sentences[i]
            sent = "".join([letter for letter in sent if letter not in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—»«"])
            words += word_tokenize(sent)
    return words

def task2(text):
    words = getWordsListFromText(text)
    morph = MorphAnalyzer()
    for i in range(100):
        print(str(morph.parse(words[i])) + "\n")

path = "dataset.txt"
file = open(path, "r", encoding="utf8")
text = file.readlines()

task2(text)