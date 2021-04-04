
import random
size = int(input())


randomArray = []
while len(randomArray) <= size:
    rand = random.randint(0, size)
    if rand not in randomArray:
        randomArray.append(rand)

print(randomArray)
print(set(randomArray))
