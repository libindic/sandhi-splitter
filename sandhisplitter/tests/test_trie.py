from testtools import TestCase
from sandhisplitter.util import head_tail
from sandhisplitter.trie import Trie


class TestTrie(TestCase):
    def setUp(self):
        super(TestTrie, self).setUp()
        self.testTrie = Trie()

    def dfs(self, node, prefix, output):
        if node == self.testTrie.end:
            output.append(prefix)
        for key in node.next.keys():
            prefix2 = prefix + node.next[key].character
            self.dfs(node.next[key], prefix2, output)

    def all_words(self):
        output = []
        self.dfs(self.testTrie.root, '', output)
        return output

    def debug(self):
        output = []
        self.dfs(self.testTrie.root, '', output)
        for word in output:
            print(word)

    def contains_substr(self, node, word):
        if not word:
            return '$' in node.next.keys()
        head, tail = head_tail(word)
        if head not in node.next.keys():
            return False
        return self.contains_substr(node.next[head], tail)

    def contains(self, word):
        return self.contains_substr(self.testTrie.root, word)
