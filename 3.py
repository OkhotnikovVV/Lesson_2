# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input("Введите номер месяца: "))
my_dict = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11]
}
my_list = ["winter", "spring", "summer", "autumn"]
for index in range(0, len(my_list)):
    try:
        my_dict.get(my_list[index]).index(month)
        print(my_list[index])
    except ValueError:
        pass

