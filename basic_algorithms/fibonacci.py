import time

def fibonacci_with_memo(num: int):
    if num == 0:
        return 0
    memo = [0] * (num+1)
    return helper(memo, num)

def helper(memo: dict, num: int):
    if num == 1 or num == 2:
        return 1
    if memo[num] != 0:
        return memo[num]
    memo[num] = helper(memo, num-1) + helper(memo, num-2)
    return memo[num]

def fibonacci(num: int):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


def fibonacci_with_dp(num: int):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    dp = [0] * (num+1)
    dp[1] = dp[2] = 1
    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[num]

def fibonacci_with_dp_optimize(num: int):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    prev, curr = 1, 1
    for _ in range(3, num+1):
        sum = prev + curr
        prev = curr
        curr = sum
    return sum

num = input("your input number (memo): ")
start_time = time.time()
ans = fibonacci_with_dp_optimize(int(num))
end_time = time.time()
execution_time = end_time - start_time
print(ans)
print(f"{execution_time:.6f} 秒")

# num = input("your input number: ")
# start_time = time.time()
# ans = fibonacci(int(num))
# end_time = time.time()
# execution_time = end_time - start_time
# print(ans)
# print(f"{execution_time:.6f} 秒")