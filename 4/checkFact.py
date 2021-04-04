def is_factorial(n):
    i = f = 1
    while f < n:
        i += 1
        f *= i
        print(f, i)
    return f == n


if is_factorial(int(input("Enter a number : "))):
    print("Yes")
