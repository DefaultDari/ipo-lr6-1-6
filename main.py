#Написать программу, которая:
#- Создаёт случайный список из **20** значений по **4** случайных целых чисел от **-10** до **10**.
#- Находит все уникальные комбинации пар из этих значений и выводит их в виде списка кортежей.
#- Пользователь вводит целое число.
#- Вычисляет количество пар, чья сумма меньше заданного пользователем значения.

import random # Модуль рандом
randlist1 = [[random.randint(-10,10) for i in range(4)]for j in range(20)] # Список в диапозоне от -10 до 10, 20 случайных значений по 4 числа
randlist2 = [] # Список
counter = 0 # Счетчик
number = int(input("Введите число: ")) # Запрашиваем число у пользователя     
for a in randlist1: # Цикл
    if a not in randlist2: # Добавление уникальных пар
        randlist2.append(a)  # Добавление    
    if sum(a) < number: # Цикл
        counter += 1 # Увеличение счётчика       
print(randlist1) # Вывод на экран
print(f"Уникальные значения {tuple(randlist2)}") # Вывод на экран
print("Кол-во пар, чья сумма меньше:",counter) # Вывод на экран
