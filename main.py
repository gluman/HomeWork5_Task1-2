"""
 p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

# названия переменных в функциях и основном блоке сознательно использую одни и теже. Я понимаю, что в функциоях названия переменных можно было использовать другое.
# Но так как они в функции переопределены, то имена оставил те же.
"""

def show_owner():
    num_doc = input('Введите номер документа: ')
    for row in documents:
        if num_doc in row.values():
            print(f"Владелец документа: {row['name']}")
            return 1
        return 0


def show_shelf():
    num_doc = input('Введите номер документа: ')
    for shelf, nums_doc in directories.items():
        if num_doc in nums_doc:
            print(f'Документ находится на полке: {shelf}')
            return (1)
    print("- Ошибка поиска документа")
    return 0


def show_docs():
    print('Перечень документов:')
    row_str = ''
    for row in documents:
        for key in row.keys():
            if key == "type":
                row_str += row[key]
        else:
            row_str += " \"" + row[key] + "\""

    print(row_str)
    return 1


def add_doc():
    num_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    name_owner = input('Введите имя владельца: ')
    num_shelf = input('Введите номер полки для хранения: ')

    dict_temp = {}  # временный словарь
    if check_doc(num_doc) != 1:  # Инверсия, если документ уже есть, то продложать нельзя.
        if check_shelf(num_shelf) == 1:  # Инверсия, если полки нет, то продложать нельзя.
            dict_temp['type'] = type_doc
            dict_temp['number'] = num_doc
            dict_temp['name'] = name_owner
            directories[num_shelf].append(num_doc)
            documents.append(dict_temp)
            return (1)
        else:
            if input(f'- Полка с номером {num_shelf} не найдена. Добавить? (yes/no): ').lower() in ['yes', 'y']:
                add_shelf(num_shelf)
                return add_doc(num_doc, type_doc, name_owner,
                               num_shelf)  # вызов из функции самой себя. Возможно ошибка. На сколько корректно такое использование? По идее работает
    else:
        print('- Документ с таким номером уже есть!')
        show_docs()
        return (0)
    print("- Документ не добавлен")
    return 0


def delete_doc():
    num_doc = input('Введите номер документа: ')
    if check_doc(num_doc):
        for row in documents:
            if num_doc in row.values():
                for s_docs in directories.values():
                    if num_doc in s_docs:
                        s_docs.remove(num_doc)
                        documents.remove(row)
                        print(f'.Документ с номером {num_doc} удален')
                        return 1
        return 0


def move_doc():
    num_doc = input('Введите номер документа: ')
    num_shelf = input('Введите номер новой полки для перемещения: ')
    if check_doc(num_doc):
        if check_shelf(num_shelf):
            for s_docs in directories.values():
                if num_doc in s_docs:
                    s_docs.remove(num_doc)
                    directories[num_shelf].append(num_doc)
                    print(f'Документ с номером {num_doc} перемещен на полку №{num_shelf}')
                    return 1
        else:
            if input(f'- Полка с номером {num_shelf} не найдена. Добавить? (yes/no): ').lower() in ['yes', 'y']:
                add_shelf(num_shelf)
                return move_doc(num_doc, num_shelf)  # вызов из функции
    else:
        print('- Ошибка перемещения документа')
        return 0


def show_shelfs():
    for key, values in directories.items():
        print(f'Полка №{key}:, Документы: {values}')
    return 1


def add_shelf():
    num_shelf = input('Введите новый номер полки для создания: ')
    if check_shelf(num_shelf) == 0:
        directories[num_shelf] = []
        print(f'Полка с номером №{num_shelf} добавлена.')
        return 1
    else:
        print(f'Полка с номером №{num_shelf} уже есть!')
        return 0


def check_doc(num_doc):  # проверка наличия документа в перечне документов и на полке
    for row in documents:
        if num_doc in row.values():
            return 1  # возвращаем true если документ найден.
    return 0 # возвращаем false если документ не найден.


def check_shelf(num_shelf):  # проверка наличия полки
    for shelf in directories:
        if num_shelf == shelf:
            return (1)
    return 0


def help_fync():
    print('''
    "h" - help - вывод справки
    "p" – people – по номеру документа и выведет имя человека, которому он принадлежит;
    "s" – shelf – по номеру документа выведет номер полки, на которой он находится;
    "l" – list – выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    "a" – add – добавление нового документа в каталог и в перечень полок.
    "d" – delete – по номеру документа удалит полностью документ из каталога и его номер из перечня полок. 
    "m" – move – по номеру документа и целевой полке переместит его с текущей полки на целевую.
    "ss" - show shelfs - вывод всех полок с номерами документов
    "as" – add shelf – по номеру новой полки добавит ее в перечень.
    "q" - quit - выход из программы
    ''')
    return 0


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
    }

command = {
    'h': help_fync(),
    'p': show_owner(),
    's': show_shelf(),
    'l': show_docs(),
    'd': delete_doc(),
    'm': move_doc(),
    'ss': show_shelfs(),
    'as': add_shelf(),
    'q': quit()
    }

run = True
while run:
    var = input('Введите команду (h или help - справка)')
    command[var]



