import faker
from random import randint

import connect

NUMBER_USERS = 5
NUMBER_TASKS = 30


def generate_fake_data(number_users, number_tasks):
    statuses = [('new',), ('in progress',), ('completed',)]
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(number_tasks):
        fake_tasks.append((fake_data.sentence(nb_words=3), fake_data.paragraph(nb_sentences=3)))

    return statuses, fake_users, fake_tasks


def prepare_data(statuses, users, tasks):
    users_len = len(users)
    statuses_len = len(statuses)
    for_tasks = []

    for task in tasks:
        for_tasks.append((*task, randint(1, statuses_len), randint(1, users_len)))

    return statuses, users, for_tasks


def insert_data_to_db(statuses, users, tasks) -> None:
    with connect.create_connection() as con:
        cur = con.cursor()

        sql_to_statuses = """INSERT INTO status(name)
                               VALUES (%s)"""

        cur.executemany(sql_to_statuses, statuses)

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (%s, %s)"""

        cur.executemany(sql_to_users, users)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                              VALUES (%s, %s, %s, %s)"""

        cur.executemany(sql_to_tasks, tasks)

        con.commit()


if __name__ == "__main__":
    statuses, users, tasks = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(statuses, users, tasks)
