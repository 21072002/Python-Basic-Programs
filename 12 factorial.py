#factorial using recursion.
def factorialfun(num):
    if num == 0:
        return 1
    else:
        return num * factorialfun(num-1)

print(factorialfun(5))
