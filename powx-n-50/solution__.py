class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        result = 1
        current_product = x

        # n is even: x^n = x^(n/2)^2
        # n is odd: x^n = x * x^((n-1)/2)^2

        # k digits 1 in binary n
        # n represents as 2^i_0 + 2^i_1 + ... + 2^i_k-1
        # pow(x, n) equals x^2^i_0 * x^2^i_1 * ...
        while n > 0:
            if n & 1:
                result *= current_product
            current_product *= current_product
            n >>= 1

        return result
