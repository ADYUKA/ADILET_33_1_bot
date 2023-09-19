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
        self.connection.execute(sql_queries.CREATE_BAN_USERS_TABLE_QUERY)

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

    def sql_insert_ban_users_command(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USERS_QUERY,
            (None, telegram_id, 1,)
        )
        self.connection.commit()

    def sql_select_ban_users_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_update_count_ban_users_command(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()