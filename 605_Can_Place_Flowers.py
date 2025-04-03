from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # booleans to check previous and next positions
        prevN = False
        nextN = False

        # Counter to increment if the flower can be planted
        count = 0
 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prevN = i==0 or flowerbed[i-1]==0
                nextN = i==len(flowerbed)-1 or flowerbed[i+1]==0

                # check if but are true, then we can plant a flower
                if prevN and nextN:
                    
                    flowerbed[i]=1
                    count += 1
                # end if
            # end if
        # end for

        return count >= n
        