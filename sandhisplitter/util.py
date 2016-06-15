# -*- coding: utf-8 -*-


def head_tail(L):
    if len(L) == 0:
        raise IndexError
    elif len(L) == 1:
        return (L[0], [])

    return (L[0], L[1:])


def extract(line):
    """Function to separate elements from string"""
    # No, not writing regexes.
    word, rest = line.split('=')
    # Split String, Location String
    ssplits, slocs = rest.split('|')
    splits = ssplits.split('+')
    locs = map(int, slocs.split(','))
    return (word, splits, locs)


def split_word_at_locations(word, locs):
    start = 0
    plain_splits = []
    for i in locs:
        part = word[start:i+1]
        plain_splits.append(part)
        start = i+1
    part = word[start:len(word)]
    plain_splits.append(part)
    return plain_splits

vowelT = {
    u'ാ': u'ആ',
    u'ി': u'ഇ',
    u'ീ': u'ഈ',
    u'ു': u'ഉ',
    u'ൂ': u'ഊ',
    u'െ': u'എ',
    u'േ': u'ഏ',
    u'ൈ': u'ഐ',
    u'ൊ': u'ഒ',
    u'ോ': u'ഓ',
    u'ൗ': u'ഔ'
}
