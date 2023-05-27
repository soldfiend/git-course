def search(myList, item):
    low = 0
    high = len(myList) - 1
    while low <= high:
        mid = (low + high) // 2
        guest = myList[mid]
        if guest == item:
            return mid
        if guest > item:
            high = mid - 1
        else:
            low = mid + 1
        return None


myList = [1, 2, 3, 6, 9, 4]
print(search(myList, 3))
