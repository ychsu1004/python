def calc_fib(n):
    if n < 2:
        return n
    else:
        return calc_fib(n-1) + calc_fib(n-2)

fib = int(input("input a number:"))
for i in range(fib):
    print(calc_fib(i), end=' ')