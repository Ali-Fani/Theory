import sys


def checkValidity(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


if __name__ == "__main__":
    if checkValidity(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])):
        print("Triangle is Valid")
    else:
        print("Triangle is not valid")
