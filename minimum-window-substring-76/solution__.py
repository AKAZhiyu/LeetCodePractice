from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result_left, result_right = 0, len(s)
        t_counter = Counter(t)
        temp_counter = Counter()

        left = 0
        for right, c in enumerate(s):
            temp_counter[c] += 1
            while temp_counter >= t_counter:
                if result_right - result_left > right - left:
                    result_left, result_right = left, right
                temp_counter[s[left]] -= 1
                left += 1

        return "" if result_right == len(s) else s[result_left: result_right + 1]




