""" This script contains functions used in Week 2 """
from IPython.display import HTML, display
import tabulate

def create_vocabulary(corpus, ys, sumvals=True):
    """ create vocabulary as `(word, class)=freq` """
    vocabulary = {}
    unique_words = {}
    total_pos = 0
    total_neg = 0
    for sentence, y in zip(corpus, ys):
        sent = sentence.split()
        for word in sent:
            pair = (word, y)
            unique_words[word] = ''
            vocabulary[pair] = vocabulary.get(pair, 0) + 1
            if y:
                total_pos += 1
            else:
                total_neg += 1
    if sumvals:
        return vocabulary, unique_words, total_pos, total_neg
    return vocabulary


def show_vocabulary(vocabulary, new_column=None, clname=''):
    d = {}
    table = [('word', 'freqPos', 'freqNeg')]
    if new_column:
        table = [('word', 'freqPos', 'freqNeg', clname)]
    total = {0: 0, 1: 0}
    for word, cl in sorted(vocabulary):
        freq = vocabulary[(word, cl)]
        if not word in d:
            d[word] = {0: 0, 1:0}
        d[word][cl] = freq
        total[cl] += freq
    if new_column:
        table += [(w, d[w][1], d[w][0], new_column[w]) for w in d]
        table.append(('TOTAL', total[1], total[0], sum(new_column.values())))
    else:
        table += [(w, d[w][1], d[w][0]) for w in d]
        table.append(('TOTAL', total[1], total[0]))
    display(HTML(tabulate.tabulate(table, tablefmt='html')))
