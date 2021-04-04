def is_factorial(n):
    i = f = 1
    while f < n:
        i += 1
        f *= i
    return f == n


check = is_factorial(int(input("Enter a number : ")))
if check:
    print("Yes")
