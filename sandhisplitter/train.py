"""
Code to train the model using dataset
"""

from trie import Trie
import sys
import json


def usage():
    string = "%s <datafile>" % (sys.argv[0])
    out = "Usage:\n" + string
    return out


def extract(line):
    """Function to separate elements from string"""
    # No, not writing regexes.
    word, rest = line.split('=')
    # Split String, Location String
    ssplits, slocs = rest.split('|')
    splits = ssplits.split('+')
    locs = map(int, slocs.split(','))
    return (word, splits, locs)

try:
    data = open(sys.argv[1], 'r', encoding='utf-8')
    line_number = 0
    try:
        for line in data:
            line_number += 1
            word, splits, locs = extract(line)
    except:
        print("Input file syntax error in line %d" % (line_number))

except IndexError:
    print("Please specify input file.")
    print(usage())

except IOError:
    print("File not found")
    print(usage())
