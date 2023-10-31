from typing import List

class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = {}
        count = 0
        for num in nums:
            if k - num in num_dict and num_dict[k-num] > 0:
                count += 1
                num_dict[k-num] -= 1
            else:
                num_dict[num] = num_dict.get(num, 0) + 1
        return count
    
class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_num = sorted(nums)
        count = 0
        i, j = 0, len(nums) - 1
        while i < j:
            if sorted_num[i] + sorted_num[j] == k:
                count += 1
                i += 1
                j -= 1
            elif sorted_num[i] + sorted_num[j] < k:
                i += 1
            else:
                j -= 1

        return count
    
sol = Solution1()
print(sol.maxOperations(nums = [1,2,3,4], k=5))

