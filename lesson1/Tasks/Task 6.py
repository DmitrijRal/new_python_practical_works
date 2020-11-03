# Спортсмен занимается ежедневными пробежками. В первый день его результат составил
# a километров. Каждый день спортсмен увеличивал результат на 10 % относительно
# предыдущего. Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров. Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
a = int(input("Enter 1st day progress(km): "))
b = int(input("Enter your goal(km): "))

day = 1
while b >= a:
    a *= 1.1
    day += 1
print(day)

#                                 Second way
#import math

#firstDayResult = int(input("Enter 1st day progress(km): "))


#goal = int(input("Enter your goal(km): "))
#increment = 1.1

#print(math.ceil(math.log(goal / firstDayResult, increment)) + 1)