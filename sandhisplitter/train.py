"""
Code to train the model using dataset
"""

import sys
from sandhisplitter.model import Model
from sandhisplitter.util import extract
import json


def usage():
    string = "%s <datafile>" % (sys.argv[0])
    out = "Usage:\n" + string
    return out

if __name__ == '__main__':
    try:
        data = open(sys.argv[1], 'r', encoding='utf-8')
        line_number = 0
        M = Model(int(sys.argv[3]), int(sys.argv[4]))
        try:
            for line in data:
                line_number += 1
                word, splits, locs = extract(line)
                M.add_entry(word, splits, locs)
        except:
            print("Input file syntax error in line %d" % (line_number))
            raise

        with open("model.json", "w", encoding='utf-8') as fp:
            json.dump(M.serialize(), fp)

        testdata = open(sys.argv[2], 'r', encoding='utf-8')
        output = open('output', 'w', encoding='utf-8')
        for line in testdata:
            line = line.strip()
            line_orig = line
            sps = M.probable_splits(line)
            splits = []
            prev = 0
            for sp in sps:
                splits.append(line[prev:sp])
                prev = sp
            splits.append(line[prev:])
            outstring = line_orig + '='
            outstring += '+'.join(splits) + '|'
            outstring += ','.join(map(str, sps))
            output.write(outstring + '\n')

    except IndexError:
        print("Please specify input file.")
        print(usage())

    except IOError:
        print("File not found")
        print(usage())
