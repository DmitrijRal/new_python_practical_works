# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("task2.txt", "r", encoding="UTF-8") as my_f:
    line_number = 1

    for line in my_f.readlines():
        print(f"Line number {line_number}. Word count: {len(line.split(' '))}")
        line_number += 1

    print(f"Lines count: {line_number - 1}")
