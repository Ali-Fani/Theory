userinput = []
for i in range(20):
    userinput.append(int(input(f"Enter Number :({i+1} out of 20) ")))
for i in range(len(userinput)):
    userinput[i] = userinput[i]-5
print(f"User input array each element -5 : {userinput}")
print(f"Smallest Number of array : {min(userinput)}")
print(f"Largest Number of array : {max(userinput)}")
