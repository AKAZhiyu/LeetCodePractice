from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            anagrams_dict[''.join(sorted(s))].append(s)
        return list(anagrams_dict.values())