from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # two minimums to check for
        first_min = float('inf')
        second_min = float('inf')

        for i in nums:
            # if i is less than or equal first_min, then re-assign it
            if i <= first_min:
                first_min = i
            # if i is less than first_min, but not less than or equal to second_min, then re-assign second_min
            elif i <= second_min:
                second_min = i
            # if i is less than first_min and second_min, then return True
            else:
                return True
            # end if
        # end for

        return False
        