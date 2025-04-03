class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        min_len = min(len(word1), len(word2))

        # Merge characters alternately
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])

        # Append the remaining part of the longer word
        merged.append(word1[min_len:])
        merged.append(word2[min_len:])

        return "".join(merged)