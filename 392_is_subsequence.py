class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True

        i = 0
        s_len = len(s)

        for char in t:
            if char == s[i]:
                i += 1
            if i == s_len:
                return True
        
        return False