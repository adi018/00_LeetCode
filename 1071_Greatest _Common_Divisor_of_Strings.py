from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Check if forward and reverse are equal
        if str1 + str2 != str2 + str1:
            return ""
        # end if

        # Calculate GCD of their lengths
        n = gcd(len(str1), len(str2))
        return str1[:n]
        