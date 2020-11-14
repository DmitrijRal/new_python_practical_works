# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

monthNumber = int(input('Input month number like 1: ')) - 1

monthsList = [
    'Winter',
    'Winter',
    'Spring',
    'Spring',
    'Spring',
    'Summer',
    'Summer',
    'Summer',
    'Autumn',
    'Autumn',
    'Autumn',
    'Winter',
]

monthsDictionary = {
    0: 'Winter',
    1: 'Winter',
    2: 'Spring',
    3: 'Spring',
    4: 'Spring',
    5: 'Summer',
    6: 'Summer',
    7: 'Summer',
    8: 'Autumn',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Winter',
}

print('List', monthsList[monthNumber])
print('Dictionary', monthsDictionary[monthNumber]