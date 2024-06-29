from pymongo import MongoClient
from pymongo.server_api import ServerApi


def db_error(func):
    """
    intercepts all exception, can be used as decorator
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Sorry, an exception occurred :: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@db_error
def read(args, db):
    """
    :param args: provide zero agrs to show all cats, one arg to show cat by name
    :param db: link to db
    :return: result in user-friendly manner
    """
    cats = []
    if len(args) == 0:
        result = db.cats.find({})
        for el in result:
            cats.append(el)
    elif len(args) == 1:
        result = db.cats.find({"name": args[0]})
        for el in result:
            cats.append(el)
    else:
        return "wrong read command args"
    return cats


@db_error
def update_age(args, db):
    """
    :param args: first arg is cat's name, second is new age that will be parsed to int
    :param db: link to db
    :return: user-friendly massage
    """
    if len(args) == 2:
        name = args[0]
        try:
            age = int(args[1])
        except ValueError:
            return "wrong update_age command args"
        r = db.cats.update_one({"name": name}, {"$set": {"age": age}})
        return "Success" if r.matched_count == 1 else "Cat not found"
    else:
        return "wrong update_age command args"


@db_error
def add_feature(args, db):
    """
    :param args: first arg is cat's name, rest will be joined to the feature string
    :param db: link to db
    :return: user-friendly massage
    """
    if len(args) >= 2:
        name = args[0]
        feature = " ".join(args[1:])
        r = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
        return "Success" if r.matched_count == 1 else "Cat not found"
    else:
        return "wrong add_feature command args"


@db_error
def delete(args, db):
    """
    :param args: provide zero agrs to delete all docs, one arg to delete cat by name
    :param db: link to db
    :return: result in user-friendly manner
    """
    if len(args) == 0:
        db.cats.delete_many({})
        return "Success"
    elif len(args) == 1:
        result = db.cats.delete_one({"name": args[0]})
        return "Success" if result.deleted_count == 1 else "Cat not found"
    else:
        return "wrong delete command args"


def main():
    client = MongoClient(
        "mongodb+srv://goithw3:QzXdg1wRDs6rS6Pa@hw3.99d0ci6.mongodb.net/?retryWrites=true&w=majority&appName=hw3",
        server_api=ServerApi('1')
    )

    db = client.cats

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "read":
            print(read(args, db))

        elif command == "update_age":
            print(update_age(args, db))

        elif command == "add_feature":
            print(add_feature(args, db))

        elif command == "delete":
            print(delete(args, db))


if __name__ == "__main__":
    main()
