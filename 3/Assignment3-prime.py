def isPrime(num: int):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                # print(i, "times", num//i, "is", num)
                # break
        else:
            return True


def getDivisors(n):
    Divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            Divisors.append(i)
    Divisors.append(n)
    return Divisors


userInput = int(input("Enter A number : "))
if isPrime(userInput):
    print("Its Prime")
else:
    print(getDivisors(userInput))
