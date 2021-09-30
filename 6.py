# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

t1 = int(input("Введите количество товаров: "))
t4 = int(input("Введите количество характеристик: "))
dict = {}
all_product = []
key_dict = []
for i in range(0,t1):
    for j in range(0,t4):
        t2 = input(f"Введите характеристику {i + 1} товара: ")
        key_dict.append(t2)
        t3 = input("Введите значение этой характеристики: ")
        dict[t2] = t3
        product = (i + 1, dict)
        dict = {}
        all_product.append(product)
result_list = []
print(key_dict)

for i in range(len(key_dict)):
    for j in range (0, t1):
        if all_product[j][1].get(key_dict[i]):
            result_list.append(all_product[j][1].get(key_dict[i]))
            print("1")
    print(key_dict[i], result_list)
    result_list = []



