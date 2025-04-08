class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        result = 0
        for num in num_set:
            if num - 1 not in num_set:
                seq_len = 1
                while num + 1 in num_set:
                    seq_len += 1
                    num += 1
                result = max(result, seq_len)
        return result
