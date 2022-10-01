def add_check(surname, name, number, pos, salary):
    whole = f'Фамилия: {surname}; Имя: {name}; Телефон: {number}; Должность: {pos}; Зарплата: {salary}\n'
    lst = whole.split('; ')
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()
    # e = open('Employees.txt', 'a', encoding='utf-8')
    for line in data_base:
        data = line.split('; ')
        k = data[1:]
        if lst == k:
            return True
        else:
            break


def add_data(surname, name, number, pos, salary):
    whole = f'Фамилия: {surname}; Имя: {name}; Телефон: {number}; Должность: {pos}; Зарплата: {salary}\n'
    lst = whole.split('; ')
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()
    e = open('Employees.txt', 'a', encoding='utf-8')
    s = ''
    last_line = data_base[-1]
    if last_line.startswith('\n'):
        last_l = data_base[-2]
        last_l = last_l.split('; ')
        lst.insert(0, str(int(last_l[0]) + 1))
        new_line = '; '.join(lst)
        s = f'{new_line}'
        e.writelines(f'{s}')
    else:
        last_line1 = last_line.split('; ')
        lst.insert(0, str(int(last_line1[0]) + 1))
        new_line = '; '.join(lst)
        s = f'{new_line}'
        e.writelines(f'{s}')
    e.close()


def view():
    with open('Employees.txt', 'r', encoding='utf-8') as mf:
        read = mf.read()
    return read


def edit_surname(id, new_data):
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()
    e = open('Employees.txt', 'w', encoding='utf-8')
    s = ''
    for line in data_base:
        if line.startswith(f'{id}'):
            data = line.split('; ')
            data[1] = f'Фамилия: {new_data}'
            # data[1] = data[1].replace(f'{current}', f'{new_data}')
            new_line = '; '.join(data)
            s += f'{new_line}'
        else:
            s += f'{line}'
    e.writelines(f'{s}')
    e.close()


def edit_name(id, new_data):
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()
    e = open('Employees.txt', 'w', encoding='utf-8')
    s = ''
    for line in data_base:
        if line.startswith(f'{id}'):
            data = line.split('; ')
            data[2] = f'Имя: {new_data}'
            new_line = '; '.join(data)
            s += f'{new_line}'
        else:
            s += f'{line}'
    e.writelines(f'{s}')
    e.close()


def edit_number(id, new_data):
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()
    e = open('Employees.txt', 'w', encoding='utf-8')
    s = ''
    for line in data_base:
        if line.startswith(f'{id}'):
            data = line.split('; ')
            data[3] = f'Телефон: {new_data}'
            # data[1] = data[1].replace(f'{current}', f'{new_data}')
            new_line = '; '.join(data)
            s += f'{new_line}'
        else:
            s += f'{line}'
            e.writelines(f'{s}')
    e.close()

   
def edit_position(ident, new_data):
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()
    e = open('Employees.txt', 'w', encoding='utf-8')
    s = ''
    for line in data_base:
        if line.startswith(f'{ident}'):
            data = line.split('; ')
            data[4] = f'Должность: {new_data}'
            # data[1] = data[1].replace(f'{current}', f'{new_data}')
            new_line = '; '.join(data)
            s += f'{new_line}'
        else:
            s += f'{line}'
            e.writelines(f'{s}')
    e.close()


def delete_data(identifier):
    with open('Employees.txt', 'r', encoding='utf-8') as e:
        data_base = e.readlines()

    with open('Employees.txt', 'w', encoding='utf-8') as f:
        for line in data_base:
            if line.startswith(f'{identifier}'):
                with open('archive.txt', 'a', encoding='utf-8') as n:
                    n.writelines(f'{line}')
            if not line.startswith(f'{identifier}'):
                f.write(line)


def calc_check(ident):
    e = open('Employees.txt', 'r', encoding='utf-8')
    data_base = e.readlines()
    for line in data_base:
        if line.startswith(f'{ident}'):
            return line


def calc(ident, norm, worked):
    # e = open('Employees.txt', 'r', encoding='utf-8')
    data = calc_check(ident).split('; ')
    lst = data[5].split()
    num_list = [int(num) for num in filter(lambda num: num.isnumeric(), lst)]
    sal = num_list[0]
    result = round(sal / norm * worked, 2)
    return str(result)
