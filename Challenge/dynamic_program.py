def fibonacci(n):
    memo = {0: 0, 1: 1}

    def fib(num):
        if num in memo:
            return memo[num]
        else:
            memo[num] = fib(num - 1) + fib(num - 2)
            return fib(num-1) + fib(num-2)
    return fib(n)


result = fibonacci(5)
print(result)
