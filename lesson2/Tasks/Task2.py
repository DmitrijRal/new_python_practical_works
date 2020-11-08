# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем
# месте. Для заполнения списка элементов необходимо использовать функцию input().

myList = input('Input numbers split by space, like `1 2 3 4 5 6 7`: ').split(' ')

cnt = 0

while cnt < len(myList):
    if cnt % 2 == 1:
        myList[cnt], myList[cnt - 1] = myList[cnt - 1], myList[cnt]

    cnt += 1

print(myList)
