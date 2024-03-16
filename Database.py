import psycopg2
from psycopg2.extras import execute_values


def database_decorator(method):
    def wrapper(self, *args, **kwargs):
        try:
            self.connect()
            result = method(self, *args, **kwargs)
            return result
        finally:
            self.disconnect()

    return wrapper


class DatabaseHandler:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")

        except psycopg2.Error as e:
            print("Unable to connect to the database:", e)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    @database_decorator
    def execute_query(self, *args):
        try:
            self.cursor.execute(*args)
            self.connection.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print("Error executing query:", e)
            self.connection.rollback()

    @database_decorator
    def execute_many(self, query, data):
        try:
            self.cursor.executemany(query, data)
            self.connection.commit()
            print("Many records inserted successfully")
        except psycopg2.Error as e:
            print("Error executing many query:", e)
            self.connection.rollback()

    @database_decorator
    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            print("Error fetching data:", e)
