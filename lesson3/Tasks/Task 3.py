# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
def my_fun(a,b,c):
    return a + b + c - (min(a,b,c))
print(my_fun(a,b,c))
