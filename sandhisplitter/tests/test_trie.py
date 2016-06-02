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

    def test_add_word(self):
        self.testTrie.add_word('hello')
        self.assertEqual(self.contains('hello'), True)
        self.assertEqual(self.contains('hell'), False)
        self.assertEqual(len(self.all_words()), 1)
        self.testTrie.add_word('temporary')
        self.assertEqual(len(self.all_words()), 2)
        self.testTrie.add_word('hell')
        self.assertEqual(len(self.all_words()), 3)
        self.assertEqual(self.contains('hell'), True)

    def test_P_sp(self):
        self.testTrie.add_word('thisistest')
        self.assertEqual(self.testTrie.P_sp('hello'), 0)
        self.assertEqual(self.testTrie.P_sp('hellow'), 0)
        self.assertEqual(self.testTrie.P_sp('thisistest'), 1)
        self.assertEqual(self.testTrie.P_nsp('thisi'), 1)
        self.testTrie.add_word('thisistest2')
        self.assertEqual(self.testTrie.P_sp('thisistest'), 0.5)

    def test_serialize(self):
        self.testTrie.add_word('thisistest')
        self.testTrie.add_word('thisistest2')
        self.testTrie.add_word('hello')

    def test_smoothed_probability(self):
        words = ['hell', 'he', 'hello', 'helsinki']
        for word in words:
            self.testTrie.add_word(word)
