class Solution1:
    def reverseWords(self, s: str) -> str:
        temp = str()
        s = s.strip()
        words_list = []
        for i in s:
            if i != ' ':
                temp += i    
            elif temp == "":
                continue
            else:
                words_list.append(temp)
                temp = str()
        
        words_list.append(temp)
        words_list.reverse()

        return ' '.join(words_list)
    

class Solution2:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)
    
s = "a good   example"
ans = Solution2()
print(ans.reverseWords(s))