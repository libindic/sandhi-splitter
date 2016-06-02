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


def transliterate(word):
    vowelT = {
        'ാ': 'ആ',
        'ി': 'ഇ',
        'ീ': 'ഈ',
        'ു': 'ഉ',
        'ൂ': 'ഊ',
        'െ': 'എ',
        'േ': 'ഏ',
        'ൈ': 'ഐ',
        'ൊ': 'ഒ',
        'ോ': 'ഓ',
        'ൗ': 'ഔ'
    }
    return vowelT
