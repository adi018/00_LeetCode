from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dict1 = defaultdict(int)
        for i in grid:
            dict1[str(i)] += 1
        # end for

        col_grid = []

        for i in range(len(grid[0])):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            # end for
            col_grid.append(temp)
        # end for

        dict2 = defaultdict(int)
        for i in col_grid:
            dict2[str(i)] += 1
        # end for

        count = 0
        for k, v in dict1.items():
            if k in dict2.keys():
                count += dict1[k] *dict2[k]
            # end if
        # end for

        print(grid)
        print(col_grid)
        return count
