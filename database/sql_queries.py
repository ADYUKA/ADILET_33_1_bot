CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FIRST_NAME CHAR(50),
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""

CREATE_ANSWER_BUTTON_TABLE = '''
        CREATE TABLE IF NOT EXISTS users_answer_button
        (ID INTEGER PRIMARY KEY,
        TG_ID INTEGER,
        USERNAME CHAR(50),
        FIRST_ANSWER CHAR(50),
        UNIQUE (TG_ID)
        )
'''


CREATE_BAN_USERS_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS ban_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        COUNT INTEGER,
        UNIQUE (TELEGRAM_ID)
        )
"""

INSERT_USER_QUERY = '''INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?)'''
INSERT_ANSWER = '''INSERT OR IGNORE INTO users_answer_button VALUES(?,?,?,?)'''
INSERT_BAN_USERS_QUERY = '''INSERT OR IGNORE INTO ban_users VALUES(?,?,?)'''

SELECT_BAN_USER_QUERY = '''
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
'''

UPDATE_BAN_USER_COUNT_QUERY = '''
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
'''