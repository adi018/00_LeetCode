class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j=0
        count = 0

        for ele in s:
            while j < len(t):
                if t[j] == ele:
                    count += 1
                    j += 1
                    break
                # end if
                j += 1
            # end while
        # end for

        return len(s) == count
        