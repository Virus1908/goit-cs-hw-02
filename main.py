from collections import UserDict


class Field:
    def __init__(self, value, is_mandatory):
        self.value = value
        self.is_mandatory = is_mandatory

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value, True)


class Phone(Field):
    def __init__(self, value):
        length = 0
        for char in value:
            if char.isdigit():
                length += 1
            else:
                raise ValueError
        if length != 10:
            raise ValueError
        super().__init__(value, False)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for stored_phone in self.phones:
            if stored_phone.value == phone:
                return stored_phone
        raise KeyError

    def remove_phone(self, phone):
        stored_phone = self.find_phone(phone)
        self.phones.remove(stored_phone)

    def edit_phone(self, prev_phone, new_phone):
        self.remove_phone(prev_phone)
        self.add_phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        self.data.pop(name)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Name or phone is not found"
        except IndexError:
            return "Please add more arguments"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts[name]
    return phone


def show_all(contacts):
    all_records = []
    for name in contacts.keys():
        all_records.append(f'{name}: {contacts[name]}')
    return "\n".join(all_records)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
