def calc_fib(num):
    if num <= 1:
        return 1
    return calc_fib(num - 1) + calc_fib(num - 2)


num = int(input())
print(calc_fib(num))