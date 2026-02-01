"""Factorial of n"""

# def factorial(val):
#     if val == 0:
#         return 1
#     return val * factorial(val-1)

# res = factorial(5)
# print(res)


"""Fibonacci sequence"""
# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)

# print(fibo(6))


"""Adding digits"""
def addSum(num, sumN=0):
    if num == 0:
        return sumN
    sumN += num%10
    num//=10
    return addSum(num,sumN)

def addDigits(num):
    if num<10:
        return num
    newSum = addSum(num)
    return addDigits(newSum)

print(addDigits(1239))