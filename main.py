from collections import defaultdict
from datetime import datetime

_day_names = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
}


def get_birthdays_per_week(users):
    result = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days >= 7:
            continue
        weekday = birthday_this_year.weekday()
        if weekday >= 5:
            weekday = 0
        result[weekday].append(name)
    for weekday in range(5):
        if len(result[weekday]) == 0:
            continue
        print(_day_names[weekday] + ": " + ", ".join(result[weekday]))


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    stored_phone = contacts.get(name)
    if stored_phone is None:
        return f"Cannot find contact for {name}"
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if phone is None:
        return f"Cannot find contact for {name}"
    else:
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
