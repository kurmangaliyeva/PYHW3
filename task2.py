# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



def pairs(list):
  list_pairs = []
  count = -1
  i = 0
  len_list = len(list) // 2

  while i < len_list:
    list_pairs.append(list[i] * list[count])
    count -= 1
    i += 1
  return list_pairs

list = [2, 3, 4, 5, 6]
list_pairs = pairs(list)
print(list)
print(list_pairs)
