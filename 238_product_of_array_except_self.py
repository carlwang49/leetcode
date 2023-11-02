from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time complexity: O(n^2)
        """
        ans = 1
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[j] != 0:
                        ans *= nums[j]
                    else:
                        ans = 0
            answer.append(ans)
            ans = 1

        return answer


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time complexity: O(n)
        """
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        answers = [0] * n

        left_product = 1
        for i in range(0, n, 1):
            left_products[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]

        for i in range(n):
            answers[i] = left_products[i] * right_products[i]

        return answers


class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l2r = [1] * n
        r2l = [1] * n
        answer = [0] * n

        current_val = 1
        for i in range(n):
            current_val *= nums[i]
            l2r[i] = current_val

        current_val = 1
        for i in range(n - 1, -1, -1):
            current_val *= nums[i]
            r2l[i] = current_val

        for i in range(n):
            if i == 0:
                answer[i] = r2l[i + 1]
            elif i == n - 1:
                answer[i] = l2r[i - 1]
            else:
                answer[i] = l2r[i - 1] * r2l[i + 1]

        return answer


nums = [-1, 1, 0, -3, 3]
ans = Solution3()
print(ans.productExceptSelf(nums))
