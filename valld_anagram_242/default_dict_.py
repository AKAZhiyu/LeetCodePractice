class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(lambda: 0)
        t_dict = defaultdict(lambda: 0)

        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1

        return s_dict == t_dict


