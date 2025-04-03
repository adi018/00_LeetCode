from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest_gain = 0
        sum_height = 0
        for i in range(len(gain)):
            sum_height += gain[i]
            highest_gain = max(highest_gain, sum_height)
        # end for

        return highest_gain

        