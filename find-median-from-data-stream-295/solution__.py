import heapq


class MedianFinder:

    def __init__(self):
        self.A = [] # max heap, smaller half, having one more element than B when odd, taking negative value
        self.B = [] # min heap, greater half

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heapq.heappush(self.A, -heapq.heappushpop(self.B, num))
        else:
            heapq.heappush(self.B, -heapq.heappushpop(self.A, -num))

    def findMedian(self) -> float:
        return -self.A[0] if len(self.A) != len(self.B) else (-self.A[0] + self.B[0]) / 2
