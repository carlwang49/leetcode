import math

class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        thoughts:
        1. 先找出兩個 strings 的其長度之最大公因數
        2. 隨便找其中一個 strings 的前綴 x, 前綴的長度為最大公因數
        3. 判斷 str1 和 str2 是否都可以由 x 取代, 若可以，則返回 x。   
        """
        len1, len2 = len(str1), len(str2)
        gcd_of_length = math.gcd(len1, len2) # find the length of great common divisor of two string 
        
        x = str1[:gcd_of_length]

        if str1.replace(x, "") == "" and str2.replace(x, "") == "":
            return x
        else:
            return ""
        

class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        題目:
        找出 str1, str2 的最大公因字串, 若沒有則返回空字串
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[:math.gcd(len(str1), len(str2))]
    

str1 = "ABABAB"
str2 = "ABAB"

solution = Solution1()
print(solution.gcdOfStrings(str1, str2))