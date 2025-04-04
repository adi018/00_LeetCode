from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                count += 1
                i += 1
                j-= 1
            # end if
        # end while
        return count
        