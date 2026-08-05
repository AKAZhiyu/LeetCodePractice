class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        result = 0
        left, right = 0, x // 2

        while left <= right:
            mid = left + (right - left + 1) // 2
            if mid * mid <= x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result




