import connect


def query1(user_id):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT * from tasks 
            WHERE user_id=%s
            ''',
            [user_id]
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query2(status):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT * FROM tasks 
            WHERE status_id=(SELECT id FROM status WHERE name=%s)
            ''',
            [status]
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query3(task_id, new_status):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            UPDATE tasks
            SET status_id=(SELECT id FROM status WHERE name=%s)
            WHERE id=%s
            ''',
            [new_status, task_id]
        )
        con.commit()


def query4():
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT * FROM users 
            WHERE id NOT IN (SELECT user_id FROM tasks)
            '''
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query5(user_id, title, description):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            INSERT INTO tasks(user_id, title, description) 
            VALUES(%s,%s,%s);
            ''',
            [user_id, title, description]
        )
        con.commit()


def query6():
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT * FROM tasks 
            WHERE status_id != (SELECT id FROM status WHERE name='completed')
            '''
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query7(task_id):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            DELETE FROM tasks WHERE id=%s
            ''',
            [task_id]
        )
        con.commit()


def query8(email):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT * FROM users
            WHERE email LIKE %s
            ''',
            [email]
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query9(user_id, new_name):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            UPDATE users
            SET fullname=%s
            WHERE id=%s
            ''',
            [new_name, user_id]
        )
        con.commit()


def query10():
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT COUNT(*), s.name
            FROM tasks t
            LEFT JOIN status s ON t.status_id = s.id
            GROUP BY s.id;
            '''
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query11(email_sufix):
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT *
            FROM tasks t
            INNER JOIN users u ON t.user_id = u.id
            WHERE u.email LIKE %s
            ''',
            [f'%@{email_sufix}']
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query12():
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT *
            FROM tasks 
            WHERE (description = '') IS NOT FALSE
            '''
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query13():
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT u.fullname, t.title
            FROM tasks t
            INNER JOIN users u ON t.user_id = u.id
            WHERE status_id=(SELECT id FROM status WHERE name='in progress')
            '''
        )
        r = cur.fetchall()
        print(r)
        con.commit()


def query14():
    with connect.create_connection() as con:
        cur = con.cursor()
        cur.execute(
            '''
            SELECT COUNT(*), u.fullname
            FROM tasks t
            LEFT JOIN users u ON t.user_id = u.id
            GROUP BY u.id;
            '''
        )
        r = cur.fetchall()
        print(r)
        con.commit()


if __name__ == "__main__":
    query14()
