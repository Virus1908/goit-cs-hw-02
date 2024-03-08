import pickle
from collections import UserDict, defaultdict
from datetime import datetime

_day_names = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
}


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


class Birthday(Field):
    def __init__(self, value):
        parsed_date = datetime.strptime(value, '%d.%m.%Y').date()
        super().__init__(parsed_date, False)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

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

    def clear_phones(self):
        self.phones.clear()

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
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
def add_contact(args, book: AddressBook):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    if len(record.phones) == 0:
        raise KeyError
    record.clear_phones()
    record.add_phone(phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    phone = book.find(name).phones[0]
    return phone


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    birthday = book.find(name).birthday
    return birthday


def birthdays(book: AddressBook):
    next_week_birthdays = defaultdict(list)
    today = datetime.today().date()
    for name, record in book.data.items():
        birthday = record.birthday
        if birthday is None:
            continue
        birthday_this_year = birthday.value.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.value.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days >= 7:
            continue
        weekday = birthday_this_year.weekday()
        if weekday >= 5:
            weekday = 0
        next_week_birthdays[weekday].append(name)
    result = []
    for weekday in range(5):
        if len(next_week_birthdays[weekday]) == 0:
            continue
        result.append(_day_names[weekday] + ": " + ", ".join(next_week_birthdays[weekday]))
    if len(result) == 0:
        return "No birthdays next week"
    return "\n".join(result)


def show_all(book: AddressBook):
    all_records = []
    for name in book.keys():
        record = book.find(name)
        birthday = "" if record.birthday is None else "Birthday at " + str(record.birthday)
        all_records.append(f'{name}: Phone - {record.phones[0]} {birthday}')
    return "\n".join(all_records)


def save(book: AddressBook):
    with open("book", "wb") as fh:
        pickle.dump(book, fh)
    return "Saved"


def main():
    try:
        with open("book", "rb") as fh:
            book = pickle.load(fh)
    except FileNotFoundError:
        book = AddressBook()

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
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        elif command == "all":
            print(show_all(book))
        elif command == "save":
            print(save(book))
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
