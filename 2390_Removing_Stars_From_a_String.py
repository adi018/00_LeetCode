class Solution:
    def removeStars(self, s: str) -> str:
        st = []

        for i in s:
            if i == '*':
                if len(st):
                    st.pop()
                # end if
            else:
                st.append(i)
            # end if
        # end for

        return ''.join(st)

        