from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i_zero = 0
        i_num = 0

        while i_zero < len(nums) and i_num < len(nums):

            while i_zero<len(nums) and nums[i_zero] != 0:
                i_zero += 1
            # end while

            i_num = i_zero + 1
            while i_num<len(nums) and nums[i_num] == 0:
                i_num += 1
            # end while

            if i_zero < len(nums) and i_num < len(nums):
                nums[i_zero] = nums[i_num]
                nums[i_num] = 0
                i_zero += 1
            # end if
        # end while
        