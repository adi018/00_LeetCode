class Solution:
    def reverseWords(self, s: str) -> str:
        # Split s by white spaces
        s = s.split()
        # reverse it and then join it
        s = s[::-1]
        
        return ' '.join(s)
        