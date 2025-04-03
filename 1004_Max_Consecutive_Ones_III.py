from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        count = 0
        for i in range(len(nums)):
            end = i
            if nums[i] == 0:
                count += 1
            # end if

            if count > k:
                if nums[start] == 0:
                    count -= 1
                # end if

                start += 1
            # end if
        # end for
        print(end, start)
        return end - start + 1