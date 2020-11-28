# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task4.txt", "r", encoding="utf-8") as f_obj1,\
        open("task4.txt", "a", encoding="utf-8") as f_obj2:
    for line in f_obj1:
        new_line = line.split(' — ')
        new_line[0] = my_dict.get(new_line[0])
        f_obj2.write(" — ".join(new_line))
