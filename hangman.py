from words import hard_words, easy_words, normal_words
import time
import random

print('Привет, давай сыграем в игру "Угадай слово"')

instr = input('Тебе нужна инструкция?  ')
if instr.lower() == 'да':
    instructions = [
        "Игра 'Виселица' - это классическая игра в слова.",
        "Компьютер случайным образом выбирает слово, и ваша задача - угадать его, называя по одной букве за раз.",
        "Если вы называете букву, которая есть в слове, компьютер показывает вам, где она находится.",
        "Если вы называете букву, которой нет в слове, попыток становится меньше",
        "Если попытки закончились, это 7 неправильных ответов, вы проиграли.",
        "Если вы угадываете все буквы в слове, прежде чем потритете попытки, вы выиграли!",
        "Удачи!"
    ]

    for line in instructions:
        print(line)
        time.sleep(3)
else:
    print('Хорошо')

print('Перейдем к игре')
time.sleep(1)
level = input('Какой уровень ты хочешь. 1 - легкие слова, 2 - нормальные слова, 3 - тяжелые слова')
if level == '1':
    secret_word = random.choice(easy_words)
elif level == '2':
    secret_word = random.choice(normal_words)
elif level == '3':
    secret_word = random.choice(hard_words)

print('Генерирую слово...')
time.sleep(2)

guessed_word = ['*' for _ in secret_word]

tries = 0
while tries <= 7:
    print(''.join(guessed_word))
    letter = input('Введи букву:  ')
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed_word[i] = letter
        if '*' not in guessed_word:
            print('Ты выиграл')
            break
    else:
        print('Такой буквы нет')
        tries += 1
else:
    print('Ты проиграл')
    print(secret_word)
