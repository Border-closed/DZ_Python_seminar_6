# Задача 1
#Создайте список из случайных чисел. Посчитайте количество уникальных элементов
#Пример.Сгенерирован массив [2, 2, 3, 0]. Количество уникальных элементов 3

from random import randint
s=[randint(0,9) for i in range(10)]
print(s)
unik=set(s)
print(f'Уникальные элементы в списке это {unik} , их коичество {len(unik)}')