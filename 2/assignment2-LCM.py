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


def computeLCM(x, y):
    lcm = (x*y)//computeGCD(x, y)
    return lcm


if __name__ == "__main__":
    print(computeLCM(int(input("Enter First Number: ")),
                     int(input("Enter First Number: "))))
