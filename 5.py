# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [7, 5, 3, 3, 2]
while True:
    element = int(input("Введите новый элемент рейтинга: "))
    rating.append(element)
    rating = sorted(rating, reverse=True)
    print(rating)
