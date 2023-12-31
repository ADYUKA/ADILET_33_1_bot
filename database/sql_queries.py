CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FIRST_NAME CHAR(50),
        LAST_NAME CHAR(50),
        REFERENCE_LINK TEXT NULL,
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

CREATE_FSM_FORM_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS user_form
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        BIO TEXT,
        AGE INTEGER,
        OCCUPATION TEXT,
        MARRIED CHAR(50),
        PHOTO TEXT,
        UNIQUE (TELEGRAM_ID)
        )
'''


CREATE_USER_COMPLAIN_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS user_complain
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID_COMPLAINED_USER INTEGER,
        TELEGRAM_ID_BAD_USER INTEGER,
        REASON TEXT,
        COUNT INTEGER,
        UNIQUE (TELEGRAM_ID_COMPLAINED_USER, TELEGRAM_ID_BAD_USER)
        )
'''


CREATE_REFERENCE_USERS_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS reference_users
        (ID INTEGER PRIMARY KEY,
        OWNER_TELEGRAM_ID INTEGER,
        REFERRAL_TELEGRAM_ID INTEGER,
        UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
        )
'''

INSERT_USER_QUERY = '''INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?,?)'''
INSERT_ANSWER = '''INSERT OR IGNORE INTO users_answer_button VALUES(?,?,?,?)'''
INSERT_BAN_USERS_QUERY = '''INSERT OR IGNORE INTO ban_users VALUES(?,?,?)'''
INSERT_USER_FORM_QUERY = """INSERT OR IGNORE INTO user_form VALUES (?,?,?,?,?,?,?,?)"""
INSERT_BAD_USER_QUERY = '''INSERT INTO user_complain VALUES(?,?,?,?,?)'''
INSERT_REFERRAL_USER_QUERY = '''INSERT INTO reference_users VALUES(?,?,?)'''

SELECT_BAN_USER_QUERY = '''
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
'''
SELECT_USER_FORM_QUERY = '''
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
'''
SELECT_ALL_USERS_QUERY = '''
SELECT * FROM telegram_users WHERE username = ?
'''
SELECT_COMPLAIN_USER_QUERY = '''
SELECT * FROM user_complain
'''
SELECT_USER_QUERY = '''
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
'''
SELECT_OWNER_BY_LINK_QUERY = '''
SELECT TELEGRAM_ID FROM telegram_users WHERE REFERENCE_LINK = ?
'''
SELECT_LIST_REFERRAL_BY_OWNER_ID_QUERY = '''
SELECT REFERRAL_TELEGRAM_ID FROM reference_users WHERE OWNER_TELEGRAM_ID = ?
'''


UPDATE_BAN_USER_COUNT_QUERY = '''
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
'''
UPDATE_BAD_USER_COUNT_QUERY = '''
UPDATE user_complain SET COUNT = COUNT + 1 WHERE TELEGRAM_ID_BAD_USER = ?
'''
UPDATE_USER_LINK_GENERATION_QUERY = '''
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
'''