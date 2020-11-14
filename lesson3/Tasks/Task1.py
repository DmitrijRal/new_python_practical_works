# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

x = float(input("Enter devider: "))
y = float(input("Enter denominator: "))
def devision_two_numbers(x, y):
    try:
        return float(x / y)
    except ZeroDivisionError:
        print("Enter another number(not zero)")
        y = float(input("Enter denominator: "))
        return float(x / y)

print(devision_two_numbers(x, y))