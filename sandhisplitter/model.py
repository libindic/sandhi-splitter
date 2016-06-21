from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from sandhisplitter.trie import Trie


class Model:
    def __init__(self, *args, **kwargs):
        if "model" in kwargs.keys():
            self.clean_init(0, 0)
            self.load(kwargs["model"])
        elif "depth" in kwargs.keys() and "skip" in kwargs.keys():
            self.clean_init(kwargs["depth"], kwargs["skip"])
        else:
            raise ValueError

    def clean_init(self, k, i):
        self.left = Trie()
        self.right = Trie()
        self.initial_skip = i
        self.k = k

    def add_entry(self, word, split, locs):
        flag = [False for i in range(len(word)+10)]
        for i in locs:
            flag[i] = True
        for i in range(1, len(word)-2):
            first, second = word[:i+1], word[i+1:]
            first = self.trim(first[::-1])
            second = self.trim(second)
            self.left.add_word(first, flag[i])
            self.right.add_word(second, flag[i])

    def serialize(self):
        return {
                "k": self.k,
                "initial_skip": self.initial_skip,
                "left": self.left.serialize(),
                "right": self.right.serialize()
                }

    def load(self, serialized):
        self.k = serialized["k"]
        self.initial_skip = serialized["initial_skip"]
        self.left.load(serialized["left"])
        self.right.load(serialized["right"])

    def probable_splits(self, word):
        ps = []
        for i in range(2, len(word)-1):
            fi, si = max(0, i-self.k-1), min(len(word), i+self.k)
            first, second = word[fi:i], word[i:si]
            backwardk = first[::-1]
            forwardk = second
            P_lsp = self.left.smoothed_P_sp(backwardk, self.initial_skip)
            P_rsp = self.right.smoothed_P_sp(forwardk, self.initial_skip)

            if (P_lsp + P_rsp >= 1.0):
                ps.append(i-1)
        return ps

    def trim(self, word):
        return word[:min(len(word), self.k)]
