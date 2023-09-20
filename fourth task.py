# №4

import random

def play_again():
    while True:
        choice = input("Хотите сыграть еще раз? (да/нет): ")
        if choice.lower() == 'да':
            return True
        elif choice.lower() == 'нет':
            return False
        else:
            print("Неверный выбор. Попробуйте еще раз.")

def main():
    print("Добро пожаловать в игру Угадай число! надо загадать с 1 до 100")
    while True:
        number = random.randint(1, 100)
        tries = 10
        print(f"У вас {tries} попыток.")
        while tries > 0:
            guess = int(input("Введите число от 1 до 100: "))
            if guess == number:
                print(f"Вы угадали число '{number}'! Кроасавчик!")
                break
            elif guess < number:
                print("Загаданное число больше.")
            else:
                print("Загаданное число меньше.")
            tries -= 1
            if tries > 0:
                print(f"Осталось {tries} попыток.")
        else:
            print(f"Вы проиграли. Загаданное число было '{number}'.")
        if not play_again():
            break
    print("Респект бро!")

if __name__ == '__main__':
    main()
