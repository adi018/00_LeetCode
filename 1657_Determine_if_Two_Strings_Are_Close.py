from collections import defaultdict
from typing import List
class Solution:


    def closeStrings(self, word1: str, word2: str) -> bool:


        if len(word1) != len(word2):
            return False
        # end if

        myWord1 = defaultdict(int)
        for word in word1:
            myWord1[word] += 1
        # end for

        myWord2 = defaultdict(int)
        for word in word2:
            myWord2[word] += 1
        # end for

        if set(word1) != set(word2):
            return False

        def findAndDelete(value1):
            for key, val in myWord2.items():
                if val == value1:
                    del myWord2[key]
                    return True
                # end if
            # end for
            return False

        for key1, value1 in myWord1.items():
            if not findAndDelete(value1):
                return False
            # end if
        # end for

        return True

        