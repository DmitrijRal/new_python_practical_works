# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем.Об окончании ввода данных свидетельствует пустая строка.

out_f = open("task1.txt", "w", encoding="UTF-8")
while True:
    write = input("Enter text: ")
    if write =="":
        break
    else:
        out_f.write(f"{write}\n")
out_f.close()
