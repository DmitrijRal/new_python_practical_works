# Пользователь вводит время в секундах. Переведите время
# в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_in_seconds = int(input("Введите время в секундах: "))
hours = time_in_seconds // 3600
seconds = time_in_seconds % 60
minutes = time_in_seconds // 60
if minutes <= 59:
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
elif minutes:
    minutes = (time_in_seconds % 3600) // 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")



