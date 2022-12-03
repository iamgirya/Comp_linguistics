from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, Doc

def norm(txt):
    _, x = map(int, txt.split('_'))
    return x

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

texts = [
    'Сам Джордж Мартин принимает непосредственное участие в создании сериала',
    'По сериалу составить портрет дракона достаточно просто',
    'В среднем масса одного крыла составляет семь процентов от общей массы тела',
    'В качестве примера полета мы выбрали сцену из девятой серии пятого сезона',
    'Всего было изучено несколько десятков образцов',
]

for text in texts:
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)

    sent = doc.sents[0]

    words = dict()
    for token in sent.tokens:
        if token.pos != 'PUNCT':
            norm_id = norm(token.id)
            words[norm_id] = token.text
            if token.rel == 'root':
                root = norm_id
    tree = {0: []}
    for k in words.keys():
        tree[k] = []
    for token in sent.tokens:
        if token.pos != 'PUNCT':
            norm_id = norm(token.id)
            norm_head_id = norm(token.head_id)
            tree[norm_head_id].append(norm_id)

    if 0 in tree.keys():
        tree.pop(0)

    sent.syntax.print() # для красоты
    print('words:', words)
    print('root:', root)
    print('tree:', tree)

    # левое скобочное пpедставление деpева
    def lrep(a):
        s = '('
        s += words[a]
        if len(tree[a]) > 0:
            for t in tree[a]:
                s += lrep(t)
        s += ')'
        return s

    # правое скобочное пpедставление деpева
    def rrep(a):
        s = '('
        # s += words[a] # отличие от ЛСПД
        if len(tree[a]) > 0:
            for t in tree[a]:
                s += lrep(t)
        s += words[a] # отличие от ЛСПД
        s += ')'
        return s

    print(lrep(root))
    print(rrep(root))

    def is_connected(i, j):
        return (i in tree[j]) or (j in tree[i])

    def is_projective():
        a = list(words.keys())
        n = len(a)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    for m in range(k + 1, n + 1):
                        if is_connected(i, k) and is_connected(j, m):
                            return False
        for i in range(1, root):
            for j in range(root + 1, n + 1):
                if is_connected(i, j):
                    return False
        return True

    print('проективное' if is_projective() else 'не проективное')
    print()
    print()

