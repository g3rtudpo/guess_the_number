import random

number = random.randint(1, 10)
guess = None
guess_count = 0
guess_limit = 5
out_of_guesses = False

print("Я загадал число от 1 до 10. У тебя есть три попытки.")

while guess != number and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("Введи число: "))
        guess_count += 1
        if guess < number:
            print("Мое число больше твоего.")
        elif guess > number:
            print("Мое число меньше твоего.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Ты проиграл. Я загадал число", number)
else:
    print("Ты выиграл! Я загадал число", number, "и тебе удалось угадать его за", guess_count, "попыток.")
