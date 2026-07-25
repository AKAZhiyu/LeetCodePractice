from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        queue = deque([startGene])
        bank = set(bank)
        if endGene not in bank:
            return -1

        steps = 0

        genes = ['A', 'C', 'G', 'T']

        while queue:
            level_length = len(queue)
            for _ in range(level_length):
                curr = queue.popleft()
                for idx, c in enumerate(curr):
                    for gene in genes:
                        if gene == c:
                            continue
                        next_gene = curr[:idx] + gene + curr[idx + 1:]
                        if next_gene == endGene:
                            return steps + 1

                        if next_gene in bank:
                            bank.remove(next_gene)
                            queue.append(next_gene)

            steps += 1

        return -1

