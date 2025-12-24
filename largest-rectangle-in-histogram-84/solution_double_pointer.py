class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        lHeightIdx, rHeightIdx = [0] * n, [0] * n
        lHeightIdx[0], rHeightIdx[-1] = -1, n

        # lHeight, rHeight = [0] * n, [0] * n
        # lHeight[0], rHeight[-1] = heights[0], heights[-1]

        for i in range(1, n):
            l = i - 1
            while l >= 0 and heights[l] >= heights[i]:
                l = lHeightIdx[l]
            lHeightIdx[i] = l

        for i in range(n - 2, -1, -1):
            r = i + 1
            while r <= n - 1 and heights[r] >= heights[i]:
                r = rHeightIdx[r]
            rHeightIdx[i] = r

        result = 0
        for i in range(n):
            # (rHeightIdx[i] - 1) - (lHeightIdx[i] + 1) - 1
            w = rHeightIdx[i] - lHeightIdx[i] - 1
            h = heights[i]
            s = w * h
            result = max(result, s)
        return result



