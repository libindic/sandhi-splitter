"""
Code to train the model using dataset
"""
import json
import argparse
from sandhisplitter.model import Model
from sandhisplitter.util import extract
from io import open

if __name__ == '__main__':  # pragma: no cover
    parser = argparse.ArgumentParser(description="Train a model")
    arguments = [
        ["-k", "--depth", "depth of the trie", int, "depth"],
        ["-s", "--skip", "initial skip", int, "skip"],
        ["-i", "--trainfile", "path to training file",
            str, "trainfile"],
        ["-o", "--outputfile", "path to store model",
            str, "modelfile"],
    ]

    for arg in arguments:
        unix, gnu, desc, typename, dest = arg
        parser.add_argument(unix, gnu, help=desc, type=typename,
                            required=True, dest=dest)

    args = parser.parse_args()
    data = open(args.trainfile, "r", encoding="utf-8")
    line_number = 0
    M = Model(depth=args.depth, skip=args.skip)
    try:
        for line in data:
            line_number += 1
            word, splits, locs = extract(line)
            M.add_entry(word, splits, locs)
    except:
        print("Input file syntax error in line %d" % (line_number))
        raise

    exported = M.serialize()
    outputfile = open(args.modelfile, "w", encoding="utf-8")
    json.dump(exported, outputfile)
