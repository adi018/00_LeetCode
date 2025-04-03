class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_vow = float('-inf')
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if i < k:
                if s[i] in vowels:
                    count += 1
                # end if
                continue
            # end if

            max_vow = max(max_vow, count)
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            # end if
        # end for

        max_vow = max(max_vow, count)
        return max_vow
        