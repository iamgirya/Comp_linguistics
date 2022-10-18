from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
)

path = "dataset.txt"
from nltk import sent_tokenize

file = open(path, "r", encoding="utf8")
text = file.readlines()
file.close()

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

words = []
for el in text:
    sentences = sent_tokenize(el)
    for number in range(len(sentences)):
        sent = sentences[number]
        doc = Doc(sent)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)
        print(doc.tokens[:5])
        doc.sents[0].syntax.print()