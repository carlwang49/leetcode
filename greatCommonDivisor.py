def gcd(a: int, b: int):
    """
    計算 a, b 的最大公因數。

    parameter:
    - a: first integer
    - b: second integer

    return:
    - great common divisor
    """

    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return a

    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


user_input1 = input("請輸入第一個數字: ")
user_input2 = input("請輸入第二個數字: ")

try:
    user_input1 = int(user_input1)
    user_input2 = int(user_input2)
    output = gcd(user_input1, user_input2)
    print(output)
except ValueError:
    print("無效的輸入，請確保輸入的數字為整數。")
