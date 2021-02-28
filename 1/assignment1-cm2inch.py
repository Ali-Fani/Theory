import sys


def cm2inch(cm: float):
    return(cm/2.52)


if __name__ == "__main__":
    print(cm2inch(float(sys.argv[1])))
