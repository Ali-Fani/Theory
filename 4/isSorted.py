inputArry = str(input("Enter An array (sperate with space) :")).split(" ")
if sorted(inputArry) == inputArry:
    print("Sorted")
else:
    print("unsorted")
