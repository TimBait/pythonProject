from itertools import groupby


def archive_string_is_alpha(string: str) -> bool:
    if not string.isalpha():                        # проверяем состоит ли входящая строка для архивации только из букв
        return False                                # нет - просим корректный ввод, да - переходим к archive_string
    return True


def restore_string_is_alnum(string: str) -> bool:     # проверяем состоит ли входящая строка для деархивации только
    if not string.isalnum() or text[0].isdigit():     # из букв + цифр и первая буква не цифра
        return False                                  # нет - просим корректный ввод, да - переходим к restore_string
    return True


def archive_string(string: str) -> str:               # собираем пару из буквы + повторений после нее
    result: list = []                                 # если повторений < 2 печатаем только букву, иначе
    for char, group in groupby(string):               # букву + количество
        group_length: int = len(list(group))
        if group_length > 1:
            result.append(f"{char}{group_length}")
        else:
            result.append(char)
    return "".join(result)


def restore_string(string: str) -> str:              # проходим по строке, на каждой итерации прибавляя индекс
    result_restore_string = ''                       # при index == длины строки цикл заканчивается
    index: int = 0                                   # внутренний цикл смотрит, является ли следующий символ
    while index < len(string):                       # цифрой и добавляет его к кол-во (+ повышает индекс итерации)
        char = string[index]                         # если след символ != цифра, к строке прибавляем
        index += 1                                   # символ * на кол-во если в кол-ве есть значение, иначе на 1
        num: str = ''
        while index < len(string) and string[index].isdigit():
            num += string[index]
            index += 1
        result_restore_string += char * (int(num) if num else 1)
    return result_restore_string


if __name__ == '__main__':
    try:
        print('Привет! Данная программа попробует заархивировать твою строку ! ')
        while True:
            user_choice: str = input('Выбери действие: Архивация строки(y) или деархивация(n)? ')
            if user_choice == 'y':
                text: str = input('Введи строку из букв для архивации без пробелов ')
                if not archive_string_is_alpha(text):
                    print('Можно ввести только буквы ! ')
                    continue
                result_archive_string: str = archive_string(text)
                print(result_archive_string)
            elif user_choice == 'n':
                text: str = input('Введи строку в формате буква+число(a2b3c4d5) либо (qw4ert6y7) ')
                if not restore_string_is_alnum(text):
                    print('Строка должна начинаться с буквы и не включать спецсимволы ! ')
                    continue
                dearchive_string: str = restore_string(text)
                if dearchive_string != text:
                    print(dearchive_string)
                else:
                    print('К сожалению вашу строку нельзя уменьшить :(' )
            else:
                print('Необходимо выбрать из двух вариантов: y или n ! ')
                continue
            end_of_work: str = input('Хотите продолжить ? (y)Да, (n)Нет ')
            if end_of_work == 'y':
                continue
            elif end_of_work == 'n':
                break
    except KeyboardInterrupt:
        print("\nПрограмма прервана.\n При необходимости запустите ее заново. ")
    finally:
        print('Всего хорошего! ')