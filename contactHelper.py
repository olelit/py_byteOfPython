from contact import *


class ContactHelper:
    __contacts = [];


    @staticmethod
    def load_сontacts():
        with open("data.txt", "r", encoding='utf-8') as ins:
            for line in ins:
                data = line.split('|')
                ContactHelper.add_contact(data[0], data[1])
            ins.close()

    @staticmethod
    def save_contacts():
        text = ""
        for item in ContactHelper.__contacts:
            text+=item.name + "|" + item.phone+"\n"
        with open("data.txt","w") as ins:
            ins.write(text)
            ins.close()

    @staticmethod
    def get_all_contact():
        for item in ContactHelper.__contacts:
            print(item.name + " " +item.phone)

    @staticmethod
    def add_contact(name, phone):
        if name != "" and phone != "":
            ContactHelper.__contacts.append(Contact(name, phone))
        else:
            return 'Заполните все данные'
        return 'Контакт успешно добавлен'

    @staticmethod
    def find_contact(phone):
        for item in ContactHelper.__contacts:
            if item.phone == phone:
                return item.name + " " +item.phone

        return 'Контакта не существует'

    @staticmethod
    def edit_contact(phone):
        for item in ContactHelper.__contacts:
            if item.phone == phone:
                print(item.name + " " +item.phone)
                print('Введите новое имя')
                item.name = input()
                print('Введите новый телефон')
                item.phone = input()
                return 'Данные изменены'

        return 'Контакта не существует'

    @staticmethod
    def delete_contact(phone):
        for item in ContactHelper.__contacts:
            if item.phone == phone:
                ContactHelper.__contacts.remove(item)
                return 'Данные успешно удалены'
        return 'Контакта не существует'


