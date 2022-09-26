import actions as act


def choice():
    while True:
        text = input('Выберите действие с данными: 1 - добавить, 2 - удалить, 3 - просмотреть, 4 - редактировать, 5 - выйти: ')
        if text == '1':
            data = input('Введите данные: Имя, Фамилия, Телефон, Должность: ')
            act.add_data(data)
        elif text == '2':
            identifier = input('Введите id для удаления данных: ')
            act.remove_data(identifier)
        elif text == '3':
            act.view_data()
        elif text == '4':
            identifier = input('Введите id для редактирования данных: ')
            current = input('Что меняем: 1 - Фамилия, 2 - Имя, 3 - Телефон, 4 - Должность')
            new = input('Введите новюую запись: ')
            act.edit_data(identifier, current, new)
        elif text == '5':
            break
        else:
            print('Введена некорректная команда.')
        

    