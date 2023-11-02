from typing import List


class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        for i in range(0, len(nums) - k + 1):
            max_avg = max(max_avg, sum(nums[i : i + k]) / k)
        return max_avg


class Solution2:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = max_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4

sol = Solution2()
print(sol.findMaxAverage(nums=nums, k=k))
