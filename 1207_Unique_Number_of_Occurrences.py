from collections import defaultdict
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map_dict = defaultdict(int)
        for i in arr:
            map_dict[i] += 1
        # end for

        return len(set(map_dict.values())) == len(list(map_dict.values()))

        