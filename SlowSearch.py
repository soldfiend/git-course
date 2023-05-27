def small(arr):
    smallest = arr[0]
    smallIndex = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallIndex = i
    return smallIndex


listArr = [10, 3, 2, 5, 1]
print(small(listArr))


# Сортировка выбором
def searchVib(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = small(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(searchVib([5, 3, 6, 2, 10]))
