def edit_data(undifier, current, new_data):
    file_base = open("Employees.txt","r") 
    data_base = file_base.readlines()
    file_base.close()
    for line in data_base:
        if line.startswith(undifier):
            data = line.split(', ')
            data[current] = new_data
            new_line = ', '.join(data)
    else:
        print(" Такого сотрудника нет. ")
