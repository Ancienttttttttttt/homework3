#Zadacha 5
# def palindorme(word):
#     word = word.lower()
#     word = word.replace(" ", "")
#     if word == word[::-1]:
#         return True
#     else:
#         return False
# word = input("Введите слово: ")
# if palindorme(word):
#     print("Слово палиндром")
# else:
#     print("Слово не палиндром")

#Zadacha 6
# num = []
# a = int(input("Введите число (0 для выхода): "))
# while a != 0:
#     num.append(a)
#     a = int(input("Введите число (0 для выхода): "))
# sum_numbers = sum(num)
# print("Сумма введенных чисел: ", sum_numbers)

#Zadacha 7
# def prostoe_chislo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# start = int(input("Введите начало диапозона: "))
# end = int(input("Введите конец диапозона: "))
#
# print("Простые числа в заданном диапазоне: ")
# for number in range(start, end + 1):
#     if prostoe_chislo(number):
#         print(number)

#Zadacha 8
# def fibo(a):
#     fib_seq = [0, 1]
#     while len(fib_seq) < a:
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#     return fib_seq
# a = int(input("Введите количество чисел Фибоначчи: "))
# print(fibo(a))

#Zadacha 9
# def triangle(fill, base):
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))
# fill = input()
# base = int(input())
# triangle(fill, base)