from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [0]*len(nums)
        # make the first element of answer as 1
        answer[0] = 1
        
        # multiply left to right
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            answer[i] = temp
        # end for

        # multiply right to left
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            answer[i] *= temp
        # end for
        print(answer)

        return answer
        