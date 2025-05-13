import random

name = input("Введите ваше имя ")

with open('name.txt', 'a') as file_name:
    file_name.write(f"{name}\n")

with open('words.txt', 'r') as file_words:
    list_word = []
    for i in file_words:
        list_word.append(i.strip())

    level_1 = list_word[0]
    level_2 = list_word[1]
    level_3 = list_word[2]
    level_4 = list_word[3]


    def shuffle_word(word):
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    counter_name = 0

    answer_1 = input(f"{name}, угадайте слово: {shuffle_word(level_1)}")
    otvet_1 = input("Введите слово: ")

    if otvet_1 == level_1:
        counter_name += 10
        print(f"Верно! Вы получаете {counter_name} очков.")
    else:
        print(f"Неверно! Верный ответ – {level_1}.")

    answer_2 = input(f"{name}, угадайте слово: {shuffle_word(level_2)}")
    otvet_2 = input("Введите слово: ")

    if otvet_2 == level_2:
        counter_name += 10
        print(f"Верно! Вы получаете {counter_name} очков.")
    else:
        print(f"Неверно! Верный ответ – {level_2}.")

    answer_3 = input(f"{name}, угадайте слово: {shuffle_word(level_3)}")
    otvet_3 = input("Введите слово: ")

    if otvet_3 == level_3:
        counter_name += 10
        print(f"Верно! Вы получаете {counter_name} очков.")
    else:
        print(f"Неверно! Верный ответ – {level_3}.")

    answer_4 = input(f"{name}, угадайте слово: {shuffle_word(level_4)}")
    otvet_4 = input("Введите слово: ")

    if otvet_4 == level_4:
        counter_name += 10
        print(f"Верно! Вы получаете {counter_name} очков.")
    else:
        print(f"Неверно! Верный ответ – {level_4}.")

with open('history.txt', 'a') as name_score:
    name_score.write(f"{name}, {counter_name}\n")

with open('history.txt', 'r') as history:
    print("***********")
    print("Список участников | Количество очков")
    histor_name_sc = history.read()
    print(histor_name_sc)

    # counter_game = []
    # for cont in histor_name_sc:
    #     counter_game.append(cont)
    #
    # print(''.join(counter_game))


    # Всего игр сыграно: 27
    # Максимальный рекорд: 200