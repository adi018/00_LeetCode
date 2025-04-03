from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        
        i = 0
        j = len(height) - 1

        max_water = float('-inf')

        while i < j:
            max_water = max(max_water, abs(j-i)*min(height[j], height[i]))

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
            # end if
        # end while
        return max_water

        