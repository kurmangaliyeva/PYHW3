# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum(list):
  sum = 0
  for i in range (1, len(list), 2):
    sum += list[i]
  return sum

list = [2, 3, 5, 9, 3]

result = sum(list)
print(list)
print(f'Сумма элементов, чтоящих на нечетной позиции = {result}')

