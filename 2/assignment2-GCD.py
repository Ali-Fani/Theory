def computeGCD(x, y):

    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        print(i)
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd


if __name__ == "__main__":
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(f"The gcd of {a} and {b} is : {computeGCD(a,b)}")
