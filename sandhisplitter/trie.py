from sandhisplitter.util import head_tail


class TrieNode:
    def __init__(self, character):
        self.character = character
        self.c_nsp = 0
        self.c_sp = 0
        self.next = {}


class Trie:
    def __init__(self):
        self.root = TrieNode('^')
        self.end = TrieNode('$')

    def update_node(self, node, word):
        if not word:
            node.next['$'] = self.end
            node.c_sp += 1
        else:
            head, tail = head_tail(word)
            if head not in node.next.keys():
                node.next[head] = TrieNode(head)
            self.update_node(node.next[head], tail)
            node.c_nsp += 1

    def add_word(self, word):
        wordList = list(word)
        self.update_node(self.root, wordList)

    def P_sp(self, word):
        """Returns probability of word being prefix to split point"""
        wordList = list(word)
        node = self.root
        while(wordList):
            head, tail = head_tail(wordList)
            wordList = tail
            if head not in node.next.keys():
                return 0
            node = node.next[head]
        return (node.c_sp/(node.c_sp + node.c_nsp))

    def P_nsp(self, word):
        return 1 - self.P_sp(word)

    def serialize_node(self, node):
        """ Serialize the tree rooted at node """
        if node == self.end:
            return '$'
        serialized = {
                "character": node.character,
                "c_sp": node.c_sp,
                "c_nsp": node.c_nsp,
                "next": {}
        }
        for child in node.next.keys():
            serialized["next"][child] = self.serialize_node(node.next[child])
        return serialized

    def serialize(self):
        """ Wrapper to make things neat """
        return self.serialize_node(self.root)
