class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            n = self.getNewNum(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)

    def getNewNum(self, n: int):
        newNum = 0
        while n:
            n, r = divmod(n, 10)
            newNum += r ** 2
        return newNum
