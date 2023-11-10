import option
import sys
import time

def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Найти абонента по номеру телефона',
          '4. Добавить абонента в справочнике',
          '5. Изменить контакт',
          '6. Удалить запись',
          '7. Закончить работу', sep='\n')
    choice = input("Выберите опцию: ")
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as ph:
        for i in ph:
            values = i.strip().split(',')
            record = dict(zip(fields, values))
            phone_book.append(record)
    return phone_book


def work_with_phonebooke():
    choice = show_menu()
    while choice != 7:
        if choice.isdigit() == False:
            print("\nНедопустимый выбор. Выберите пункты от 1 до 7.\n\n")
        else:
            choice = int(choice)
            if choice == 1:
                time.sleep(2)
                # Распечатать справочник
                option.print_phone_book(read_txt("phonebook.csv"))
            elif choice == 2:
                # Найти телефон по фамилии
                option.find_phone_family(read_txt("phonebook.csv"))
            elif choice == 3:
                # Найти абонента по номеру телефона
                option.find_subscriber_by_phone(read_txt("phonebook.csv"))
            elif choice == 4:
                # Опция 4 выбрана: Добавить абонента в справочник
                option.add_subscriber_in_phonebook(read_txt("phonebook.csv"), "phonebook.csv")
            elif choice == 5:
                # Изменить контакт
                option.change(read_txt("phonebook.csv"), "phonebook.csv")
            elif choice == 6:
                # Удалить запись
                option.delete_record(read_txt("phonebook.csv"), "phonebook.csv")
            elif choice == 7:
                print(" ")
                print("Работа завершена!")
                print("Благодарю за внимание!")
                sys.exit()
            else:
                print(" ")
                print("Неверный пункт!")
                print("Выберите от 1 до 7")
            print(end="\n\n")
        choice = show_menu()

work_with_phonebooke()









