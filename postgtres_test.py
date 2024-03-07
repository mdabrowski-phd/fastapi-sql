import psycopg2

db_password = "postgres"

# ---
create_query = "create table test (a integer, b integer)"
conn = psycopg2.connect(dbname="postgres", user="postgres", password=db_password, host="localhost")
cur = conn.cursor()

cur.execute(create_query)
conn.commit()

cur.close()
conn.close()
