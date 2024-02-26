def fib(numb):
    if numb==0:
        return 0
    elif numb==1:
        return 0
    elif numb==2:
        return 1
    else:
        return fib(numb -1)+fib(numb-2)
print(fib(10))