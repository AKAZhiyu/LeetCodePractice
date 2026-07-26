from typing import List


class TrieNode:
    __slots__ = 'children', 'end'

    def __init__(self):
        self.children = {}
        self.end = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end == word

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = word

    def has_prefix(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        result = []
        rows, cols = len(board), len(board[0])

        for word in words:
            trie.insert(word)

        def dfs(i, j, trie_node):
            char = board[i][j]
            if char not in trie_node.children:
                return

            curr_node = trie_node.children[char]

            if curr_node.end is not None:
                result.append(curr_node.end)
                curr_node.end = None

            board[i][j] = '#'

            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_i, next_j = i + x, j + y
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    dfs(next_i, next_j, curr_node)

            board[i][j] = char

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root)

        return result
