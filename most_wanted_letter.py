import collections, operator, string

def checkio(text):

    letters = {s:0 for s in string.lowercase}
    letters = collections.OrderedDict(sorted(letters.items()))
    text = text.lower()

    for t in text:
        if t.isalpha():
            letters[t] += 1

    mwl = max(letters.iteritems(), key=operator.itemgetter(1))[0]

    return mwl
