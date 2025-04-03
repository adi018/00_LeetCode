class Solution:
    def reverseVowels(self, s: str) -> str:

        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']

        # Convert str to list for assignment during swapping
        s = list(s)

        while i<j:

            # Come to vowel from left
            while s[i].lower() not in vowels and i<j:
                i += 1
            # end while

            # come to vowel from right
            while s[j].lower() not in vowels and i<j:
                j -= 1
            # end while

            # swap and increment i and j
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        # end while

        return ''.join(s)
        