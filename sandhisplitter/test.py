import argparse
import json
from sandhisplitter.model import Model
from sandhisplitter.postprocessor import PostProcessor
from sandhisplitter.util import extract, compress
from operator import add


def split_error(desired, obtained):
    pass


def location_error(desired, obtained, length):
    # Set difference(A, B) = A - B
    # Set intersection(A, B) = A & B
    ds, os = map(set, [desired, obtained])
    u = set(range(1, length-1))
    true_positives = ds & os
    true_negatives = (u - ds) & (u - os)
    false_positives = os - ds
    false_negatives = (u - os) - (u - ds)
    output = (true_positives, true_negatives,
              false_positives, false_negatives)
    return map(len, output)


def measures(location_metric):
    tp, tn, fp, fn = map(float, location_metric)
    result = {}
    result["Precision"] = tp/(tp+fp)
    result["Recall"] = tp/(tp+fn)
    result["Accuracy"] = (tp+tn)/(tp+tn+fp+fn)
    result["True Negative Rate"] = tn/(tn+fp)
    return result

if __name__ == '__main__':  # pragma: no cover
    parser = argparse.ArgumentParser(description="Test a model")
    arguments = [
        ["-m", "--modelfile", "path to model file",
            argparse.FileType("r"), "modelfile"],
        ["-t", "--testfile", "path to test file",
            argparse.FileType("r"), "testfile"],
        ["-u", "--unsplit", "path to store unsplit data",
            argparse.FileType("w"), "unsplit"],
        ["-s", "--split", "path to store split data",
            argparse.FileType("w"), "split"],
    ]
    for arg in arguments:
        unix, gnu, desc, typename, dest = arg
        parser.add_argument(unix, gnu, help=desc, type=typename,
                            required=True, dest=dest)
    args = parser.parse_args()
    model = json.load(args.modelfile)
    M = Model(model=model)
    P = PostProcessor()
    output = args.split
    no_splits = args.unsplit
    stats = (0, 0, 0, 0)
    for line in args.testfile:
        line = line.strip()
        word, desired_splits, desired_locs = extract(line)
        sps = M.probable_splits(word)
        splits = P.split(line, sps)
        outstring = compress(word, splits, sps) + '\n'
        split_metrics = split_error(desired_splits, splits)
        location_metrics = location_error(desired_locs, sps, len(word))
        stats = map(add, stats, location_metrics)
        if sps:
            output.write(outstring)
        else:
            no_splits.write(outstring)
    results = measures(stats)
    print("Split point identification stats:")
    for key in results.keys():
        print('  ', key, ':', results[key])
