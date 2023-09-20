# №3

import random

def get_word():
    words = ['python', 'java', 'javascript', 'ruby', 'php', 'html', 'css']
    return random.choice(words)

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
    print("Добро пожаловать в игру Виселица!")
    while True:
        word = get_word()
        guessed_letters = set()
        tries = 6
        while tries > 0:
            print(f"У вас {tries} попыток.")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=' ')
                else:
                    print('_', end=' ')
            print()
            guess = input("Введите букву: ")
            if guess in guessed_letters:
                print("Вы уже вводили эту букву. Давай еще.")
            elif guess in word:
                guessed_letters.add(guess)
                if set(word) == guessed_letters:
                    print(f"Вы угадали слово '{word}'! Красавчик!")
                    break
            else:
                tries -= 1
                print("Такой буквы в слове нет.")
        else:
            print(f"Вы проиграли. Загаданное слово было '{word}'.")
        if not play_again():
            break
    print("Спасибо за игру!")

if __name__ == '__main__':
    main()
