# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
# фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
import itertools
from functools import reduce
with open("task3.txt", "r", encoding="UTF-8") as my_f:
    employee_count = 0
    emloyee_salary = 0
    for line in my_f.readlines():
        employee_count += 1
        sername, salary = line.split(" ")
        emloyee_salary += int(salary)
        if int(salary) < 20000:
            print(f"Employee with salary < 20000: {sername}")
    print(f"Average salary: {emloyee_salary/employee_count}")
