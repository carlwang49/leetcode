from typing import List

class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:

        def find_insert_position(sorted_nums: List[int], key: int):

            left = 0
            right = len(sorted_nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if key == sorted_nums[mid]:
                    return mid
                elif key < sorted_nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        ans = []
        ans.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                position = find_insert_position(ans, nums[i])
                ans[position] = nums[i]

            if len(ans) >= 3:
                return True
        
        return False
    

class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')
        for num in nums:
            if num <= first: # 找第一小的數字
                first = num
            elif num <= second: # 找第二小的數字
                second = num
            else:
                return True

        return False