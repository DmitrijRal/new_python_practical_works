# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input("Enter name: ")
sername = input("Enter person_sername: ")
birth_year = input("Enter birth_year: ")
birth_town = input("Enter birth_town: ")
live_town = input("Enter live_town: ")
email = input("Enter email: ")
phone_number = input("Enter phone_number: ")

def person_inf(name, sername, birth_year, birth_town, live_town, email , phone_number):
   return f"name - {name}; sername - {sername}; birth_year - {birth_year}; birth_town - {birth_town};\
   live_town - {live_town}; email - {email}; phone_number - {phone_number}"
print(person_inf(sername=sername,birth_year=birth_year,live_town=live_town,name=name,\
                 birth_town=birth_town,phone_number=phone_number, email=email))