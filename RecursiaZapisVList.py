def factorialCalculation(n, *listMain):
    if n == 0:
        return 1
    else:
        return n * factorialCalculation(n - 1)


mainList = [4, 5, 5, 0, 1]
endList = []
for i in mainList:
    end = factorialCalculation(i, *mainList)
    endList.append(end)
print('list-', endList)


