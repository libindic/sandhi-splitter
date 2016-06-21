from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from sandhisplitter.model import Model


class Splitter:
    def __init__(self, model):
        self.M = Model(model=model)

    def split(self, word, locations):
        return self.M.probable_splits(word, locations)
