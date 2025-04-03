from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Calculate max candies in candies
        max_candies = max(candies)
        
        # Check for each element in candies the condition
        answer = [(i+extraCandies >= max_candies) for i in candies]
        return answer

        
        