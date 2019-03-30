from contactHelper import *

def main():

    print('1 - Вывести все контакты')
    print('2 - добавить контакт')
    print('3 - изменить контакт')
    print('4 - удалить контакт')
    print('5 - поиск контакта')
    print('6 - сохранить контакты1')
    ContactHelper.load_сontacts()

    while (True):
        print('Выберите действие')
        option = input()
        if option == '1':
            ContactHelper.get_all_contact()
        elif option == '2':
            addContact()
        elif option == '3':
            edit_contact()
        elif option == '4':
            delete_contact()
        elif option == '5':
            search_contact()
        elif option == '6':
            save_contact()

def phone_block():
    print('Введите телефон')
    return input()

def edit_contact():
    ContactHelper.edit_contact(phone_block())

def save_contact():
    ContactHelper.save_contacts()

def search_contact():
    ContactHelper.find_contact(phone_block())


def delete_contact():
    ContactHelper.delete_contact(phone_block())


def addContact():
    print('Введите имя')
    name = input()
    ContactHelper.add_contact(name, phone_block())

main()
