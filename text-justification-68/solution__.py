from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        n = len(words)
        i = 0
        while i < n:
            start = i
            sum_len = -1
            while i < n and sum_len + len(words[i]) + 1 <= maxWidth:
                sum_len += 1 + len(words[i])
                i += 1

            extra_space = maxWidth - sum_len
            gaps = i - start - 1

            if gaps == 0 or i == n:
                tmp = ' '.join(words[start: i]) + ' ' * extra_space
                result.append(tmp)
                continue

            avg, rmd = divmod(extra_space, gaps)
            spaces = ' ' * (avg + 1)

            tmp = (spaces + ' ').join(words[start: start + rmd + 1]) + spaces + spaces.join(words[start + rmd + 1: i])
            result.append(tmp)

        return result



