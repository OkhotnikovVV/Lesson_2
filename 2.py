# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = input("Введите элементы списка, разделив их пробелами: ").split()
print(my_list)
index = 0
for index in range(0, len(my_list), 2):
    if index != len(my_list)-1:
        temp = my_list[index]
        my_list[index] = my_list[index + 1]
        my_list[index+1] = temp
print(my_list)