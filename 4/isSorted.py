inputArry = str(input("Enter An array (sperate with space) :")).split(" ")
isSorted = True
if sorted(inputArry) == inputArry:
    print("Sorted")
else:
    print("unsorted")
