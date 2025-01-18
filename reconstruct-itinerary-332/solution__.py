from typing import List, Dict
from collections import defaultdict
# works fine only onwards python 3.7 which has dict in order


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        results = ["JFK"]
        length = len(tickets) + 1
        tickets.sort(key=lambda x: x[1])  # sort the tickets list in dist lexical order
        adjacent_dict = {}
        for k, v in tickets:
            if k not in adjacent_dict:
                adjacent_dict[k] = defaultdict(int)
            adjacent_dict[k][v] += 1

        self.backtracking(results, length, adjacent_dict)
        return results

    def backtracking(self, results: List[str], length: int, adjacent_dict: Dict[str, Dict[str, int]]):
        if len(results) == length:
            return True

        current_beginning = results[-1]
        if current_beginning in adjacent_dict:
            for current_dist, times_left in adjacent_dict[current_beginning].items():
                if times_left > 0:
                    adjacent_dict[current_beginning][current_dist] = times_left - 1
                    results.append(current_dist)

                    if self.backtracking(results, length, adjacent_dict):
                        return True

                    adjacent_dict[current_beginning][current_dist] = times_left
                    results.pop()

        return False

