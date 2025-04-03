from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_num = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            if i < k:
                sum_num += nums[i]
                continue
            # end if
            max_sum = max(max_sum, sum_num)
            sum_num += (nums[i] - nums[i-k])
            
        # end for
        max_sum = max(max_sum, sum_num)
        return max_sum /k