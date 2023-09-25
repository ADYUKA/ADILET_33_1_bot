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
        self.connection.execute(sql_queries.CREATE_FSM_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_COMPLAIN_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERENCE_USERS_TABLE_QUERY)

    def sql_insert_users_command(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, None,)
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

    def sql_insert_user_form_command(self, telegram_id, nickname, bio,
                                     age, occupation, married, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, age, occupation, married, photo,)
        )
        self.connection.commit()

    def sql_select_user_form_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'bio': row[3],
            'age': row[4],
            'occupation': row[5],
            'married': row[6],
            'photo': row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_users_report_command(self, username):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2],
            'first_name': row[3],
            'last_name': row[4],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_QUERY,
            (username,)
        ).fetchall()

    def sql_insert_complain_users_command(self, telegram_id_comp_user, telegram_id_bad_user, reason):
        self.cursor.execute(
            sql_queries.INSERT_BAD_USER_QUERY,
            (None, telegram_id_comp_user, telegram_id_bad_user, reason, 1)
        )
        self.connection.commit()

    def sql_select_complain_users_command(self):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id_complained_user': row[1],
            'telegram_id_bad_user': row[2],
            'reason': row[3],
            'count': row[4],
        }
        return self.cursor.execute(
            sql_queries.SELECT_COMPLAIN_USER_QUERY,
        ).fetchall()

    def sql_update_count_bad_users_command(self, telegram_id_bad_user):
        self.cursor.execute(
            sql_queries.UPDATE_BAD_USER_COUNT_QUERY,
            (telegram_id_bad_user,)
        )
        self.connection.commit()

    def sql_select_user_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2],
            'first_name': row[3],
            'last_name': row[4],
            'link':  row[5],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_update_user_link_generation_command(self, link, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_GENERATION_QUERY,
            (link, telegram_id,)
        )
        self.connection.commit()

    def sql_insert_reference_user_command(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_USER_QUERY,
            (None, owner, referral,)
        )
        self.connection.commit()

    def sql_select_owner_by_link_command(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            'telegram_id': row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_OWNER_BY_LINK_QUERY,
            (link,)
        ).fetchall()

    def sql_select_list_referral_by_owner_id_command(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'referral_id': row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_LIST_REFERRAL_BY_OWNER_ID_QUERY,
            (owner,)
        ).fetchall()