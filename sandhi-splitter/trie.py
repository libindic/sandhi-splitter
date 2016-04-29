class TrieNode:
    def __init__(self, character):
        self.character = character
        self.c_nsp = 0
        self.c_sp = 0
        self.next = {};


class Trie:
    def __init__(self):
        self.root = TrieNode('^');
        self.end = TrieNode('$');

    def update_node(self, node, word):
        if not word:
            node.next['$'] = self.end;
            node.c_sp += 1
        else:
            #print("Adding %s"%(word))
            head, *tail = word
            if head not in node.next.keys():
                node.next[head] = TrieNode(head)
            self.update_node(node.next[head], tail)
            node.c_nsp += 1

    def dfs(self, node, prefix):
        if node == self.end:
            print(prefix)
        for key in node.next.keys():
            prefix2 = prefix + node.next[key].character
            self.dfs(node.next[key], prefix2)

    def debug(self):
        self.dfs(self.root, '')


    def add_word(self, word):
        #print("Adding %s"%(word))
        wordList = list(word)
        self.update_node(self.root, word)

    def P_sp(self, word):
        """Returns probability of word being prefix to split point"""
        wordList = list(word)
        node = self.root
        while(wordList):
            head, *tail = wordList
            wordList = tail
            if head not in node.next.keys():
                return 0
            node = node.next[head]
        return (node.c_sp/(node.c_sp + node.c_nsp));


    def P_nsp(word):
        return 1 - P_sp(word);



if __name__ == '__main__':
    x = Trie()
    x.add_word("Hello")
    x.add_word("He")
    x.add_word("Hell")
    x.add_word("What the fuck")
    x.add_word("Howareya?")
    x.add_word("How do you do?")
    print(x.P_sp("Hello"))
    print(x.P_sp("He"))
    print(x.P_sp("Hwll"))
    x.debug()
