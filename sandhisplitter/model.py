from sandhisplitter.trie import Trie


class Model:
    def __init__(self, k, i):
        self.left = Trie()
        self.right = Trie()
        self.initial_skip = i
        self.k = k

    def add_entry(self, word, split, locs):
        plain_splits = []
        start = 0
        for i in locs:
            part = word[start:i+1]
            plain_splits.append(part)
            start = i+1
        part = word[start:len(word)]
        plain_splits.append(part)
        for i in range(len(plain_splits)-1):
            first, second = plain_splits[i:i+2]
            first = self.trim(first[::-1])
            second = self.trim(second)
            self.left.add_word(first)
            self.right.add_word(second)

    def serialize(self):
        return {
                "k": self.k,
                "initial_skip": self.initial_skip,
                "left": self.left.serialize(),
                "right": self.right.serialize()
                }

    def probable_splits(self, word):
        ps = []
        for i in range(2, len(word)-1):
            fi, si = max(0, i-self.k-1), min(len(word), i+self.k)
            first, second = word[fi:i], word[i:si]
            backwardk = first[::-1]
            forwardk = second
            print("first: %s, second: %s" % (first, second))
            print("first: %s, second: %s" % (backwardk, forwardk))
            P_lsp = self.left.smoothed_P_sp(backwardk, self.initial_skip)
            P_rsp = self.right.smoothed_P_sp(forwardk, self.initial_skip)
            # P_lsp = self.left.P_sp(backwardk)
            # P_rsp = self.right.P_sp(forwardk)

            print("left: %f, right %f" % (P_lsp, P_rsp))
            print("---")
            l = (self.k-self.initial_skip)
            if (l*P_lsp >= 1.0 and l*P_rsp >= 1.0):
                ps.append(i)
        return ps

    def trim(self, word):
        return word[:min(len(word), self.k)]
