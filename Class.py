def calc_factorial(x):
    if x==1:
        return x
    else:
        return (x * calc_factorial(x-1))

num = 4

print("The factorial of",num,"is",calc_factorial(num))
