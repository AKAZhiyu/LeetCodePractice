class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        heights = [0] + heights + [0]
        n = len(heights)
        stack = [0]

        for i in range(1, n):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    idx = stack.pop()
                    if stack:
                        r = i - 1
                        l = stack[-1] + 1
                        w = r - l + 1
                        h = heights[idx]
                        result = max(w * h, result)
                stack.append(i)
        return result



