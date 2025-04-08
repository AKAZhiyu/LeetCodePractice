class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, result = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                result = max(result, (j - i) * height[i])
                i += 1
            else:
                result = max(result, (j - i) * height[j])
                j -= 1
        return result
