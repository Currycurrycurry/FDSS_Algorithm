class Trie:
    class Node:
        def __init__(self, value=value, is_word=False):
            self.map = dict()
            self.is_word = False
            self.value = value

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.map:
                node.map[char] = Node(value=char)
            node = node.map[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.map:
                return False
            node = node.map[char]
        return node.is_word

    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.map:
                return False
            node = node.map[char]
        return node



obj = Trie()
obj.insert('apple')
