import math
while True:
    op = input('please enter operator: ')
    if op == '+':
        a = int(input("please enter first number:"))
        b = int(input("please enter second number:"))
        result = a+b
    elif op == '-':
        a = int(input("please enter first number:"))
        b = int(input("please enter second number:"))
        result = a-b
    elif op == '*':
        a = int(input("please enter first number:"))
        b = int(input("please enter second number:"))
        result = a*b
    elif op == '!':
        a = int(input("please enter number:"))
        result = f'result of {a}!: {math.factorial(a)}'
    elif op == 'sin':
        a = int(input("please enter number:"))
        result = math.sin(a)
    elif op == 'tan':
        a = int(input("please enter number:"))
        result = math.tan(a)
    elif op == 'cot':
        a = int(input("please enter number:"))
        result = math.cot(a)
    elif op == 'sqrt':
        a = int(input("please enter number:"))
        result = math.sqrt(a)
    elif op == 'power':
        a = int(input("please enter number:"))
        b = int(input("please enter number:"))
        result = math.pow(a, b)
    elif op == 'log':
        a = int(input("please enter fixed number:"))
        b = input("please enter base number:default(2)")
        if not b:
            result = math.log2(a)
        else:
            result = math.log(a, int(b))
    elif op == '/':
        a = int(input("please enter first number:"))
        b = int(input("please enter second number:"))
        if b == 0:
            result = "cannot divide by zero!"
        result = a/b
    else:
        result = 'operator not found!'

    print(result)
    check = input("do you want to continue?(y/n):default(y)").lower()
    if check == 'y' or check == '':
        continue
    elif check == 'n':
        break
