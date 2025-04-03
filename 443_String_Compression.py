from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)
        idx = 0
        count = 1

        for i in range(1, n+1):
            if i < n and chars[i] == chars[i-1]:
                count += 1
            else:
                chars[idx] = chars[i-1]
                idx += 1

                if count > 1:
                    for k in str(count):
                        chars[idx] = k
                        idx += 1
                    # end for
                # end if
                count = 1
            # end if
        # end for

        print(chars, idx)
        return idx 

        