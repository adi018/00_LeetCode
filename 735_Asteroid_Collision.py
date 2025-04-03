from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []
        for asteroid in asteroids:
            if len(st)==0 or asteroid > 0:
                st.append(asteroid)
            else:
                while not len(st)==0  and st[-1] > 0 and st[-1] < -asteroid:
                    st.pop()
                # end while

                if len(st)==0  or st[-1] <0:
                    st.append(asteroid)
                elif not len(st)==0  and st[-1] == -asteroid:
                    st.pop()
                # end if    
            # end if
        # end for
        print("final", st)
        return st

        
