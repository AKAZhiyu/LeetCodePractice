class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 1
        letter_set = set()
        # start_idx, end_idx = 0, 0

        for start_idx in range(len(s)):
            letter_set.clear()
            curr_length = 0
            for end_idx in range(start_idx, len(s)):
                if s[end_idx] not in letter_set:
                    letter_set.add(s[end_idx])
                    curr_length += 1
                    max_length = max(max_length, curr_length)
                else:
                    break

        return max_length



