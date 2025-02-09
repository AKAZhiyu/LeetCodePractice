class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        int_list = list(map(int, str(n)))

        flag = len(int_list)
        for i in range(len(int_list) - 1, 0, -1):
            if int_list[i] < int_list[i - 1]:
                int_list[i - 1] -= 1
                flag = i

        for i in range(flag, len(int_list)):
            int_list[i] = 9

        result = int(''.join(map(str, int_list)))
        return result

