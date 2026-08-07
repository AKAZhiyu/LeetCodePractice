class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x >= 10 and x % 10 == 0):
            return False

        rev = 0
        origin = x

        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        return rev == origin



