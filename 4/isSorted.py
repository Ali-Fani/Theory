inputArry = str(input("Enter An array (sperate with space) :")).split(" ")


def isSorted(array):
    first = True
    for i in range(len(array)):
        if first:
            first = False
            continue
        if array[i] < array[i-1]:
            return False
    return True


Sorted = isSorted(inputArry)
if Sorted:
    print("array is sorted")
else:
    print("Array is Not Sorted")
