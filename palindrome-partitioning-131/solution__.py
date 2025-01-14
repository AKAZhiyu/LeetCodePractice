from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.backtracking(results, [], s, 0)
        return results

    def backtracking(self, results, path, s, start_idx):
        if start_idx == len(s):
            results.append(path[:])
            return

        for i in range(start_idx, len(s)):
            if self.is_palindrome(s, start=start_idx, end=i):
                path.append(s[start_idx: i + 1])
                self.backtracking(results, path, s, i + 1)
                path.pop()

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        i: int = start
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
