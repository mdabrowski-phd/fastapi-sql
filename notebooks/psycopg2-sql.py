import psycopg2


conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host='localhost')
cursor = conn.cursor()

# create_query = """CREATE TABLE tasks(
#     id SERIAL,
#     description TEXT,
#     priority SMALLINT,
#     is_complete BOOLEAN
# )
# """

# create_query = """CREATE TABLE users(
#     id SERIAL,
#     username TEXT,
#     password TEXT,
#     is_admin BOOLEAN
# )
# """

#
# cursor.execute(create_query)
# conn.commit()
#
#
# insert_queries = ["""INSERT INTO tasks(description, priority, is_complete) VALUES ('Pierwsze zadanie', 3, true)
# """, """INSERT INTO tasks(description, priority, is_complete) VALUES ('Drugie zadanie', 1, false)
# """, """INSERT INTO tasks(description, priority, is_complete) VALUES ('Trzecie zadanie', 2, true)
# """]
#
# for query in insert_queries:
#     cursor.execute(query)

# conn.commit()

# select_query = "SELECT * FROM tasks"
#
# cursor.execute(select_query)
# print(cursor.fetchone())
# print(cursor.fetchall())

# insert_queries = ["""INSERT INTO tasks(description, priority, is_complete) VALUES ('Pierwsze_1 zadanie', 3,
# true) RETURNING *""",
#                   """INSERT INTO tasks(description, priority, is_complete) VALUES ('Drugie_1 zadanie', 1,
#                   false) RETURNING *""",
#                   """INSERT INTO tasks(description, priority, is_complete) VALUES ('Trzecie_1 zadanie', 2,
#                   true) RETURNING *"""]
#
# insert_queries = ["""INSERT INTO tasks(description, priority, is_complete) VALUES ('Pierwsze_1 zadanie', 3,
# true) RETURNING id""",
#                   """INSERT INTO tasks(description, priority, is_complete) VALUES ('Drugie_1 zadanie', 1,
#                   false) RETURNING id""",
#                   """INSERT INTO tasks(description, priority, is_complete) VALUES ('Trzecie_1 zadanie', 2,
#                   true) RETURNING id"""]
#
# conn.rollback()
#
# for query in insert_queries:
#     cursor.execute(query)
#
# conn.commit()
#
# record = cursor.fetchone()
# print(record)

# SQL Injection Attack

# id_number = "1"
# query = f"UPDATE tasks SET priority = 9 WHERE id = {id_number}"
#
# cursor.execute(query)
# conn.commit()

# id_number = "1; DROP TABLE users;"
# query = f"UPDATE tasks SET priority = 12 WHERE id = {id_number}"
#
# cursor.execute(query)
# conn.commit()

# id_number = "1"
# query = "UPDATE tasks SET priority = 7 WHERE id = %s"
#
# cursor.execute(query, (id_number,))
# conn.commit()

# id_number = "1"
# query = "UPDATE tasks SET priority = %s WHERE id = %s"
#
# cursor.execute(query, (6, id_number))
# conn.commit()

# id_number = "1; DROP TABLE users"
# query = "UPDATE tasks SET priority = 3 WHERE id = %s"
#
# print(cursor.mogrify(query, (id_number,)).decode())

# cursor.execute(query, (id_number,))
# conn.commit()  # ERROR --> so we avoid SQL injection attack!
