from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        self.backtracking(results, s, 0, 0, "")
        return results

    def backtracking(self, results: List[str], s: str, points_num: int, start_idx: int, path: str):
        if points_num == 3:
            if self.is_valid(s, start_idx, len(s) - 1):
                path = path + s[start_idx:]
                results.append(path)
                return

        for i in range(start_idx, len(s)):
            if self.is_valid(s, start_idx, i):
                self.backtracking(results, s, points_num + 1, i + 1, path + s[start_idx: i + 1] + '.')
            else:
                break

    def is_valid(self, s: str, start: int, end: int):
        if start > end:
            return False
        if start != end and s[start] == '0':
            return False
        num = 0
        for i in range(start, end + 1):
            char = s[i]
            if not char.isdigit():
                return False
            num = num * 10 + int(char)
            if num > 255:
                return False
        return True

