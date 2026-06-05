class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        result = 0

        for i, c in enumerate(s):
            if c == "(":
                st.append(i)
            elif len(st) > 1:
                st.pop()
                result = max(result, i - st[-1])
            else:
                st[0] = i

        return result