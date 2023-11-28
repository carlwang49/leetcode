class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isdigit() or s[i] == '[' or s[i].isalpha():
                stack.append(s[i])
            elif s[i] == ']':
                temp_string = ""
                while stack[-1] != '[':
                    top = stack.pop()
                    temp_string = top + temp_string
                if stack[-1] == '[':
                    stack.pop() 
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                if num:
                    temp_string = temp_string * int(num)
                stack.append(temp_string)
            print(stack)
        return "".join(stack)


s = "2[abc]3[cd]ef"
sol = Solution()
ans = sol.decodeString(s)
print(ans)