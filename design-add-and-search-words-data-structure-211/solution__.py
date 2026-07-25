class Node:
    __slots__ = 'end', 'children'

    def __init__(self):
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.__dfs(word, self.root)

    def __dfs(self, word, node):
        if not word:
            return node.end
        ch = word[0]
        if ch != '.':
            if ch not in node.children:
                return False
            else:
                return self.__dfs(word[1:], node.children[ch])
        else:
            for child in node.children:
                if self.__dfs(word[1:], node.children[child]) is True:
                    return True
            return False
