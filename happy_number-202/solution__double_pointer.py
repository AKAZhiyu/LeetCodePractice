class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total

        slow, fast = n, getNext(n)

        while fast != slow and fast != 1:
            fast = getNext(getNext(fast))
            slow = getNext(slow)

        return fast == 1


