# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_list = input("Enter numbers divided by space: ")
with open("task5.txt", "w+", encoding="utf-8") as f_obj:
    f_obj.write(my_list)
    f_obj.seek(0)
    content = f_obj.readline().split(" ")
    print(sum([int(el) for el in content]))
