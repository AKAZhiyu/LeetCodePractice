# class LRUCache(object):
# python 3.7+ solution
#
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.cache = {}
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.cache:
#             return -1
#
#         value = self.cache.pop(key)
#         self.cache[key] = value
#         return value
#
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.cache:
#             self.cache.pop(key)
#         self.cache[key] = value
#
#         if len(self.cache) > self.capacity:
#             k = next(iter(self.cache))
#             self.cache.pop(k)
#         return
from collections import OrderedDict
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache.get(key)

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        return 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)