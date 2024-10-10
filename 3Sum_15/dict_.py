from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()

            for j in range(i + 1, len(nums)):

                # to avoid triplets which contain same items
                if j > i + 2 and nums[j] == nums[j - 1] == nums[j - 2]:
                    continue

                c = 0 - nums[i] - nums[j]

                if c in seen:
                    result.append([nums[i], nums[j], c])
                    seen.remove(c)
                else:
                    seen.add(nums[j])

        return result


