import psycopg2
from config import config


def connect():
    connection = None
    try:
        params = config()
        print(f'connecting to the postgresql database')
        connection = psycopg2.connect(**params)

        # create cursor
        crsr = connection.cursor()
        print('Postgresql database version:')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated")

connect()