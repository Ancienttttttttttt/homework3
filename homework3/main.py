#Zadacha 5
#while True:
#    try:
#        a = int(input("Введите число: "))
#        print("Вы ввели число ", a)
#    except:
#        print("Ошибка: вы ввели не число")

#Zadacha 6
#while True:
#    try:
#        a = int(input("Введите делимое: "))
#        b = int(input("Введите делитель: "))
#        c = a/b
#        print("Ответ: ", "{:.3f}".format(c))
#    except:
#        print("Ошибка: деление на ноль")

#Zadacha 7
# while True:
#     class NegativeNumberError(Exception):
#         pass
#     try:
#         a = int(input("Введите положительное число: "))
#         if a < 0:
#             raise NegativeNumberError
#         else:
#             print(a ** 2)
#     except NegativeNumberError:
#         print("Вы ввели отрицательное число")