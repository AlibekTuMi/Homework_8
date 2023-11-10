﻿
# 1. Распечатать справочник
def print_phone_book(file_open):
    keys_to_fio = ["Фамилия", "Имя"]
    keys_to_data = ["Телефон", "Описание"]
    for i in range(len(file_open)):
        print(i+1, end=": ")
        entry = file_open[i]
        values = [entry[key] for key in keys_to_fio]
        print(*values, end=", ")
        values = [entry[key] for key in keys_to_data]
        print(*values, end="")
        print()


# 2. Найти телефон по фамилии
def find_phone_family(file_open):
    family = input("Введите фамилию абонента: ")
    family = Higher_order(family)
    found_phone_record = []
    found_fio_record = []
    for record in file_open:
        if record.get("Фамилия") == family:
            found_phone_record.append(record.get("Телефон"))
            found_fio_record.append(record.get("Фамилия"))
            found_fio_record.append(record.get("Имя"))
    fio = " ".join(found_fio_record)
    if found_phone_record:
        for record in found_phone_record:
            print(f"Телефон абонента {fio} - {record}")
    else:
        print("Абонент не найден")


# 3. Найти абонента по номеру телефона
def find_subscriber_by_phone(file_open):
    phone = input("Введите номер телефона абонента: ")
    found_phone_record = []
    found_fio_record = []
    found_info_record = []
    for record in file_open:
        if record.get("Телефон") == phone:
            found_phone_record.append(record.get("Телефон"))
            found_fio_record.append(record.get("Фамилия"))
            found_fio_record.append(record.get("Имя"))
            found_info_record.append(record.get("Описание"))
    fio = " ".join(found_fio_record)
    info = "".join(found_info_record)
    if found_phone_record:
        for record in found_phone_record:
            print(f"Абонент {fio}. Телефон - {record}. Описание - {info}")
    else:
        print("Абонент не найден")


# 4. Добавить абонента в справочник
def add_subscriber_in_phonebook(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    family = input("Введите фамилию абонента: ")
    name = input("Введите имя абонента: ")
    phone = input("Введите номер телефона абонента: ")
    info = input("Чем занимается?: ")
    new_subscriber = [family, name, phone, info]
    new_subscriber = dict(zip(fields, new_subscriber))
    file_open.append(new_subscriber)
    # print(file_open)
    with open(filename, 'w', encoding='utf-8') as ph:
        for record in file_open:
            line = ','.join(record[field] for field in fields)
            ph.write(line + "\n")

# 5. Изменить контакт
def change(file_open, filename):
    next_change = True
    while (next_change):
        fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
        q = False
        while q == False:
            print("По какому параметру хотите производить поиск?\n1. Фамилия\n2. Имя \n3. Телефон\n4. Описание")
            q=True
            field_input = int(input())
            field_in = fields[field_input - 1]
            famile_found = input("Введите свой запрос: ")
            if field_input==1 or field_input==2:
                famile_found = Higher_order(famile_found)
            found_people = []
            id = []
            for record in range(len(file_open)):
                if file_open[record].get(field_in) == famile_found:
                    found_people.append(file_open[record])
                    id.append(record)
            if len(found_people) >= 2:
                print("Найдено больше одного запроса, выберите 1")
                for i in range(len(found_people)):
                    line = ', '.join('{} {}'.format(key, val) for key, val in sorted(found_people[i].items()))
                    print(f"{i+1} - {line}")
                vi = int(input())
                vi = vi - 1
            elif len(found_people) == 0:
            
                print("Запись не найдена!")
                print("Чтобы повторить изменение контакта нажмите Enter")
                print("Чтобы выйти в главное меню введите любой символ")
                num = input("")
                if num == "":
                    q=False
                else:
                    return 0
        if len(found_people) == 1:
            vi = 0
                
        print("Что вы хотите изменить?\n Фамилия, нажмите 1\n Имя, нажмите 2 \n Телефон, нажмите 3\n Описание, нажмите 4")
        change = int(input())
        change_in = fields[change - 1]
        new_record = input("Введите новое значение: ")
        if change==1 or change==2:
                new_record = Higher_order(new_record)
        for record in file_open:
            if record == found_people[vi]:
                record[change_in] = new_record
        with open(filename, 'w', encoding='utf-8') as ph:
            for record in file_open:
                line = ','.join(record[field] for field in fields)
                ph.write(line + "\n")
        next_input = int(input("Хотите поменять что-либо еще?\n1. Да   2. Нет\n"))
        if next_input == 2:
            next_change = False


# 6. Удалить запись
def delete_record(file_open, filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    confirm_w = False
    while (confirm_w == False):
        family = input("Введите фамилию абонента, запись о котором вы хотите удалить: ")
        found_phone_record = []
        found_fio_record = []
        found_info_record = []
        for record in file_open:
            if record.get("Фамилия") == family:
                found_phone_record.append(record.get("Телефон"))
                found_fio_record.append(record.get("Фамилия"))
                found_fio_record.append(record.get("Имя"))
                found_info_record.append(record.get("Описание"))
        fio = " ".join(found_fio_record)
        info = "".join(found_info_record)
        if found_phone_record:
            for record in found_phone_record:
                print(f"Абонент - {fio}. Телефон - {record}. Описание - {info}")
                confirm = input("Все верно?\n1 - да   2 - нет\n")
                if confirm == "1":
                    confirm_w = True
                    record_delete = 0
                    for i in range(len(file_open)):
                        if file_open[i].get("Фамилия") == family:
                            record_delete = i
                    del file_open[record_delete]
                    with open(filename, 'w', encoding='utf-8') as ph:
                        for record in file_open:
                            line = ','.join(record[field] for field in fields)
                            ph.write(line + "\n")
                else:
                    next_input = input("Хотите ввести другое значение?\n1 - да   2 - нет\n")
                    if next_input == '2':
                        confirm_w = True
        else:
            print("Абонент не найден")
            next = int(input("Продолжить?\n1. Да    2. Нет\n"))
            if next == 2:
                return 0
                
# Функция верхнего регистра первой буквы
def Higher_order(input_user):
    input_user = input_user.lower()
    input_user = list(input_user)
    input_user[0] = input_user[0].upper()
    return ''.join(input_user)
























