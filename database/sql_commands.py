import sqlite3
from database import sql_queries


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("tg_db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connection successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_ANSWER_BUTTON_TABLE)

    def sql_insert_users_command(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name,)
        )
        self.connection.commit()

    def sql_insert_answer_command(self, tg_id, username, first_answer):
        self.cursor.execute(
            sql_queries.INSERT_ANSWER,
            (None, tg_id, username, first_answer,)
        )
        self.connection.commit()
