def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

n = int(input("Enter number:  "))

print(fact(n))