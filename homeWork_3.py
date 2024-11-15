def calculate_word_score(word: object) -> object:


    english_scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
                     'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
                     'D': 2, 'G': 2,
                     'B': 3, 'C': 3, 'M': 3, 'P': 3,
                     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                     'K': 5,
                     'J': 8, 'X': 8,
                     'Q': 10, 'Z': 10}
    russian_scores = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1,
                     'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
                     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
                     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
                     'Й': 4, 'Ы': 4,
                     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
                     'Ш': 8, 'Э': 8, 'Ю': 8,
                     'Ф': 10, 'Щ': 10, 'Ъ': 10}

    if all('A' <= char <= 'Z' or 'a' <= char <= 'z' for char in word):
        scores = english_scores
    elif all('А' <= char <= 'Я' or 'а' <= char <= 'я' for char in word):
        scores = russian_scores
    else:
        print("Ошибка: слово должно содержать только англдийские или русские буквы")
        return

    total_score = sum(scores.get(char.upper(), 0) for char in word)

    return total_score

word = input("Введите слово: ")
score = calculate_word_score(word)

print(f"Вывод: {score}")

# def calculate_word_score(word):
#     # Словарь для оценки английских букв
#     english_scores = {
#         'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
#         'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#         'D': 2, 'G': 2,
#         'B': 3, 'C': 3, 'M': 3, 'P': 3,
#         'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#         'K': 5,
#         'J': 8, 'X': 8,
#         'Q': 10, 'Z': 10
#     }
#
#     # Словарь для оценки русских букв
#     russian_scores = {
#         'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#         'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#         'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#         'Й': 4, 'Ы': 4,
#         'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#         'Ш': 8, 'Э': 8, 'Ю': 8,
#         'Ф': 10, 'Щ': 10, 'Ъ': 10
#     }
#
#     # Определяем, какие буквы используются в слове
#     if all('A' <= char <= 'Z' or 'a' <= char <= 'z' for char in word):
#         scores = english_scores
#     elif all('А' <= char <= 'Я' or 'а' <= char <= 'я' for char in word):
#         scores = russian_scores
#     else:
#         print("Ошибка: слово должно содержать только английские или русские буквы.")
#         return
#
#     # Суммируем очки для каждой буквы
#     total_score = sum(scores.get(char.upper(), 0) for char in word)
#
#     return total_score
#
#
# # Чтение слова от пользователя
# word = input("Введите слово: ").upper()
# score = calculate_word_score(word)
#
# # Вывод результата
# print(f"Вывод: {score}")