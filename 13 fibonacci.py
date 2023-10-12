#fibonacci number using recursion.
def fib_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_num(num-1) + fib_num(num-2)
print(fib_num(5))