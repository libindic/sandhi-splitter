from testtools import TestCase
from testtools.content import Content
from testtools.content_type import UTF8_TEXT
import trie

class TestTrie(TestCase):
    def setUp(self):
        super(TestTrie, self).setUp()
        self.testTrie = trie.Trie()

    def dfs(self, node, prefix, output):
        if node == self.Trie.end:
            output.append(prefix)
        for key in node.next.keys():
            prefix2 = prefix + node.next[key].character
            self.dfs(node.next[key], prefix2)

    def debug(self):
        output = []
        self.dfs(self.testTrie.root, '', output)
        for word in output:
            print(word)
    
    def contains_substr(self, node, word):
        if not word:
            return '$' in node.next.keys()
        head, *tail = word
        if head not in node.next.keys():
            return False
        return self.contains_substr(node.next[head], tail)


    def contains(self, word):
        return self.contains_substr(self.testTrie.root, word);

    def test_add_word(self):
        self.testTrie.add_word('hello')
        self.assertEqual(self.contains('hello'), True)
        self.assertEqual(self.contains('hell'), False)

