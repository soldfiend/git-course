num_1 = 1
num_2 = 1
summa = 0
print(num_1,num_2)
for i in range (6):
    summa =  num_1 + num_2
    num_1 = num_2
    num_2 = summa
    print(num_2)
