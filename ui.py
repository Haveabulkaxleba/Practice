import actions as act

def choice():
    while True:
        text = input('''Выберите действие с данными:
1 - добавить сотрудника
2 - удалить сотрудника (при увольнении)
3 - просмотреть
4 - редактировать
5 - расчитать оклад сотрудника за месяц
6 - выйти из программы
Ответ: ''')
        if text == '1':
            while True:
                while True:
                    surname = input('''Введите данные.
Фамилия: ''')
                    if surname.isalpha() and surname.istitle():
                        break
                    if not surname.isalpha() or not surname.istitle():
                        print('Введите корректные символы (первая буква фамилии должна быть заглавная).')
                        continue
                while True:
                    name = input('Имя: ')
                    if name.isalpha() and name.istitle():
                        break
                    if not name.isalpha() or not name.istitle():
                        print('Введите корректные символы (первая буква имени должна быть заглавная).')
                        continue
                while True:
                    number = input('Введите номер телефона (11 цифр без пробелов): ')
                    if number.isnumeric() and len(number) == 11:
                        break
                    else:
                        print('Номер должен состоять из 11 цифр.')
                while True:
                    position = input('Укажите должность: ')
                    if position.isalpha() and position.istitle():
                        break
                    elif not position.isalpha() or not position.istitle():
                        print('Введите корректные символы (название должности должно начинать с заглавной буквы)')
                while True:
                    salary = input('Введите размер зарплаты: ')
                    if salary.isdigit():
                        break
                    else:
                        print('Используйте только цифры для указания зарплаты')
                act.add_check(surname, name, number, position, salary)
                if act.add_check(surname, name, number, position, salary):
                    print('Данные о таком сотруднике уже есть в базе. Повторите ввод.')
                elif not act.add_check(surname, name, number, position, salary):
                    act.add_data(surname, name, number, position, salary)
                    print('Данные были добавлены.')
                    break
        elif text == '2':
            ask = input('''При удалении сотрудника данные о нём будут перенесены в отдельный файл (archive.txt).
Для удаления данных необходимо указать идентификатор сотрудника в файле.
Если вы не знаете, какой идентификатор вам нужен, введите 1, чтобы запросить список данных с идентификаторами.
Если вы знаете нужный идентификатор, введите 2 для продолжения.
Ответ: ''')
            if ask == '1':
                print(act.view())
            elif ask == '2':
                identifier = input('Введите id сотрудника для удаления: ')
                act.delete_data(identifier)
        elif text == '3':
            print(act.view())
        elif text == '4':
            ask = input('''Для изменения данных необходимо указать идентификатор сотрудника в файле.
Если вы не знаете, какой идентификатор вам нужен, введите 1, чтобы запросить список сотрудников с идентификаторами.
Если вы знаете нужный идентификатор, введите 2 для продолжения.
Ответ: ''')
            if ask == '1':
                print(act.view())
            elif ask == '2':
                while True:
                    identifier = input('Введите id для редактирования данных: ')
                    if identifier.isdigit():
                        break
                    else:
                        print('Введены некорректные символы. Повторите ввод.')
                choice = input('''Выберите, что будем менять:
1 - Фамилию
2 - Имя
3 - Телефон
4 - Должность
Ответ: ''')
                while True:
                    if choice == '1':
                        surname = input('Введите новую фамилию: ')
                        if surname.isalpha() and surname.istitle():
                            act.edit_surname(identifier, surname)
                            print('Данные были изменены')
                            break
                        if not surname.isalpha() or not surname.istitle():
                            print('Введите корректные символы (первая буква фамилии должна быть заглавная).')
                    elif choice == '2':
                        name = input('Введите новое имя: ')
                        if name.isalpha() and name.istitle():
                            act.edit_name(identifier, name)
                            print('Данные были изменены')
                            break
                        if not name.isalpha() or not name.istitle():
                            print('Введите корректные символы (первая буква имени должна быть заглавная).')
                    elif choice == '3':
                        new_num = input('Введите новый номер телефона (11 цифр без пробелов): ')
                        if new_num.isnumeric() and len(new_num) == 11:
                            new = new_num.replace(' ', '')
                            act.edit_number(identifier, new)
                            print('Данные были изменены')
                            break
                        else:
                            print('Номер должен состоять из 11 цифр.')
                    elif choice == '4':
                        pos = input('Введите название новой должности: ')
                        if pos.isalpha() and pos.istitle():
                            act.edit_position(identifier, pos)
                            print('Данные были изменены')
                            break
                        elif not pos.isalpha() or not pos.istitle():
                            print('Введите корректные символы (название должности должно начинать с заглавной буквы)')
                    else:
                        print('Введены некорректные символы. Повторите ввод.')
                        break
        elif text == '5':
            ask = input('''Для удаления данных необходимо указать идентификатор сотрудника в файле.
Если вы не знаете, какой идентификатор вам нужен, введите 1, чтобы запросить список данных с идентификаторами.
Если вы знаете нужный идентификатор, введите 2 для продолжения.
Ответ: ''')
            if ask == '1':
                print(act.view())
            elif ask == '2':
                while True:
                    identifier = input('Введите id для редактирования данных: ')
                    if identifier.isdigit():
                        break
                    else:
                        print('Введены некорректные символы. Повторите ввод.')
                print('''Для расчёта укажите норму рабочего времени в целевом месяце в днях,
а также количество фактически отработанных дней за месяц''')
                try:
                    norm = int(input('Норма рабочего времени: '))
                    worked = int(input('Отработно дней: '))
                    act.calc_check(identifier)
                    if act.calc_check(identifier):
                        print('Оклад за текущий месяц: ', act.calc(identifier, norm, worked))
                    else:
                        print('Сотрудника с таким идеентификатором нет.')
                except ValueError:
                    print('Возникла ошибка при расчёте. Необходимо указать целое число.')
        elif text == '6':
            break
        else:
            print('Введена некорректная команда.')
        

    