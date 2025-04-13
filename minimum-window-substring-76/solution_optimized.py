from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        gap_counter = defaultdict(int) # gap number
        result_left, result_right = 0, len(s)
        for c in t:
            gap_counter[c] += 1

        less = len(gap_counter) # gap type

        left = 0
        for right, c in enumerate(s):
            gap_counter[c] -= 1
            if gap_counter[c] == 0:
                less -= 1

            while less == 0:
                if result_right - result_left > right - left:
                    result_right, result_left = right, left
                gap_counter[s[left]] += 1
                if gap_counter[s[left]] == 1:
                    less += 1
                left += 1

        return "" if result_right == len(s) else s[result_left: result_right + 1]


