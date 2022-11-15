import psycopg2
import sys

#  this isnt rlly working will revisit


conn = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432',
    database='postgres'
)

create_database = '''
create database testing
'''

create_table = '''
create table people(
    id serial not null,
    name varchar(30) not null
)
'''

insert_into_table = '''
insert into people(name) values ('foo barian')
'''

select_all_from_table = '''
select * from people
'''

queries = [create_table,insert_into_table,select_all_from_table]

cursor = conn.cursor()


if 'read' in sys.argv[1]:
    cursor.fetchall()
elif 'write' in sys.argv[1]:
    [cursor.execute(x) for x in queries]
