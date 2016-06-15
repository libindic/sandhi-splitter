import argparse
import json
from sandhisplitter.model import Model
from sandhisplitter.postprocessor import PostProcessor

if __name__ == '__main__':
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
    for line in args.testfile:
        line = line.strip()
        line_orig = line
        sps = M.probable_splits(line)
        splits = P.split(line, sps)
        outstring = line_orig + '='
        outstring += '+'.join(splits) + '|'
        outstring += ','.join(map(str, sps))
        if sps:
            output.write(outstring + '\n')
        else:
            no_splits.write(outstring + '\n')
