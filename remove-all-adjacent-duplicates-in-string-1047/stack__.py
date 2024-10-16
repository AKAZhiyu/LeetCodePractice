class Solution:
    def removeDuplicates(self, s: str) -> str:
        list_ = []

        for char in s:
            if len(list_) != 0 and list_[-1] == char:
                list_.pop()
            else:
                list_.append(char)

        return "".join(list_)