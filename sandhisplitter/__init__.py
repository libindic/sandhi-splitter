from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import json
from sandhisplitter.splitter import Splitter
from sandhisplitter.postprocessor import PostProcessor
from pkg_resources import resource_filename


class Wrapper:
    def __init__(self):
        modelfilename = resource_filename('sandhisplitter',
                                          'models/model.json')
        modelfile = open(modelfilename, 'r', encoding='utf-8')
        serialized = json.load(modelfile)
        modelfile.close()
        self.splitter = Splitter(model=serialized)
        self.postprocessor = PostProcessor()

    def split(self, word):
        ps = self.splitter.splits(word)
        split_words = self.postprocessor.split(word, ps)
        return (split_words, ps)

    def get_module_name(self):
        return "Sandhi-Splitter"

    def get_info(self):
        return "Sandhi-splitter for malayalam"


def getInstance():
    return Wrapper()
