from typing import List


class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #
    #     k = k % len(nums)
    #     nums[:] = nums[-k:] + nums[: -k]
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reserve(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n
        reserve(0, n - 1)
        reserve(0, k - 1)
        reserve(k, n - 1)





