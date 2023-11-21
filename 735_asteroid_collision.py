from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            cur_asteroid = asteroids[i]
            if not stack:
                stack.append(cur_asteroid)
            elif not (stack[-1] > 0 and cur_asteroid < 0):
                stack.append(cur_asteroid)
            else:
                while stack and stack[-1] > 0 and cur_asteroid < 0:
                    if abs(cur_asteroid) > abs(stack[-1]):   
                        stack.pop()
                    elif abs(asteroids[i]) == abs(stack[-1]):  
                        stack.pop()
                        cur_asteroid = 0
                    else:
                        cur_asteroid = 0
                if cur_asteroid != 0:
                    stack.append(cur_asteroid)
        
        return stack