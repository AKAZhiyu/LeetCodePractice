from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        steps = 1
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        while queue:
            level_lenth = len(queue)

            for _ in range(level_lenth):
                curr_word = queue.popleft()

                for idx, c in enumerate(curr_word):
                    for i in range(ord('a'), ord('z') + 1):
                        ch = chr(i)
                        if ch == c:
                            continue
                        next_word = curr_word[:idx] + ch + curr_word[idx + 1:]
                        if next_word == endWord:
                            return steps + 1

                        if next_word in wordSet:
                            wordSet.remove(next_word)
                            queue.append(next_word)

            steps += 1

        return 0

