
# буквы, которых точно нет в загаданном слове
bad_letters = list("багорвеник")


# буквы, которые есть в слове, но не на своих позициях, указано, какие позиции точно не подходят
right_letters = [
        # {'letter': "л", 'position': [4]},
        # {'letter': "а", 'position': [1]},
]

# буквы, которые есть в слове, и известны их точные позиции
# true_letters = [
#     {'letter': "е", 'position': [1, 3]},
#     {'letter': "ч", 'position': [2]},
#     {'letter': "с", 'position': [5, ]},
# ]

true_letters = [
    # {'letter': "у", 'position': [1]},
]


with open('data/russian_nouns.txt', 'r') as f:
    all_words = f.read().splitlines()

print("Всего слов считано из словаря", len(all_words))

five_letters = []

for i in all_words:
    if len(i) == 5:
        five_letters.append(i)

print("Из них пятибуквенных слов - ", len(five_letters))

good_words = []


def check_bad_letter(word):
    """
    Проверяет пятибуквенное слово на наличие в нём букв, которых в нём быть не должно
    :param word:
    :return:
    """
    check_bad_letter_result = []
    for bl in bad_letters:
        if word.find(bl) != -1:
            check_bad_letter_result.append('1')
    if "1" not in check_bad_letter_result:
        return True
    else:
        return False


def check_true_letter(word):
    """
    Проверяет пятибуквенное слово на наличие в нём букв, которые в нём точно есть на известной позиции
    :param word:
    :return:
    """
    check_true_letter_result = []
    for tl in true_letters:

        for p in tl['position']:

            if word[p] == tl['letter']:
                check_true_letter_result.append("1")
            else:
                check_true_letter_result.append("0")
    if "0" not in check_true_letter_result:
        return True
    else:
        return False


def check_right_letter(word):
    """
    Проверяет пятибуквенное слово на наличие в нём букв, которые в нём есть, но известна только позиция,
    на которой их быть не должно
    :param word:
    :return:
    """
    check_right_letter_result = []
    for rl in right_letters:
        if word.find(rl['letter']) != -1:

            for p in rl['position']:

                if word[p] == rl['letter']:
                    check_right_letter_result.append("0")
                else:
                    check_right_letter_result.append("1")
        else:
            check_right_letter_result.append("0")
    if "0" not in check_right_letter_result:
        return True
    else:
        return False


def five_letters_word():
    """
    Проверяет пятибуквенное слово на наличие в нём букв, которых в нём быть не должно,
    затем проверяет на наличие букв, которые в нём точно есть на известной позиции,
    затем на наличие букв, которые в нём есть, но известна только позиция, на которой их быть не должно
    :return:
    """
    for word in five_letters:
        if check_bad_letter(word) is True:

            if check_true_letter(word) is True:

                if check_right_letter(word) is True:

                    good_words.append(word)

    print("Количество подходящих слов: ", len(good_words))
    print(*good_words, sep="\n")


if __name__ == "__main__":
    five_letters_word()

