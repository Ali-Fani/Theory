# n = int(input("Enter A number for factorial : "))
n=4
factarray = []
for i in range(0, n+1):
    fact = 1
    for j in range(1, i+1):
        fact = fact * j
        print(fact)
    factarray.append(fact)

print(factarray)
