import random
import os


def creation_of_secret_list() -> list:
    """Функция создания секретного списка стотоящего из 4 целых чисел. """
    secret_list = []
    while True:
        random_number = random.randint(1, 9)
        if random_number not in secret_list:
            secret_list.append(random_number)
        if len(secret_list) == 4:
            return secret_list


def is_digits(number: str) -> bool:
    """Функция проверки на int и на число от 0 до 9"""
    try:
        if 0 <= int(number) <= 9:
            return True
        else:
            return False
    except ValueError:
        return False


def getting_list_of_user_digits() -> list:
    """Функция запроса данных у пользователя"""
    user_list = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Укажите 4 целых чилса! Указано {user_list}")
        number = input("Введите число от 0 до 9: ")
        if is_digits(number):
            user_list.append(int(number))
            if len(user_list) == 4:
                print(user_list)
                return user_list
        else:
            print(f'Введены не корректные данные "{number}"! Попробуйте езе раз!')


def cow_and_bull(secret_list: list, user_list: list) -> tuple:
    """Подсчет коров и быков"""
    cow = []
    bull = []
    counter = 0
    for i in user_list:
        if i == secret_list[counter]:
            bull.append(i)
        elif i in secret_list:
            cow.append(i)
        counter += 1
    return cow, bull


def information_output(cow: list, bull: list) -> None:
    """Вывод информации пользователю"""
    quantity_cow = len(cow)
    quantity_bull = len(bull)
    text = f"Найдено {quantity_cow} коров и {quantity_bull} быков!"
    print(text)


def main():
    secret_list = creation_of_secret_list()
    user_list = getting_list_of_user_digits()
    cow, bull = cow_and_bull(secret_list, user_list)
    information_output(cow, bull)


if __name__ == '__main__':
    main()
