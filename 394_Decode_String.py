class Solution:
    def decodeString(self, s: str) -> str:
        
        num = 0
        num_st = []
        str_st = []
        temp = ''
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10*num + int(s[i])
            elif s[i] == '[':
                num_st.append(num)
                num = 0

                str_st.append(temp)
                temp= ''
            elif s[i] == ']':
                times = num_st.pop()
                temp_2 = temp
                temp = str_st.pop() +  temp_2*times
                print(temp)
            else:
                temp += s[i]
            # end if
        # end for

        return temp
