from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        word_len = len(p)
        counter_p = Counter(p)
        counter_window = Counter(s[:word_len])

        if counter_p == counter_window:
            result.append(0)

        for i in range(word_len, len(s)):
            counter_window[s[i]] += 1
            counter_window[s[i - word_len]] -= 1

            if counter_p == counter_window:
                result.append(i - word_len + 1)
        return result






