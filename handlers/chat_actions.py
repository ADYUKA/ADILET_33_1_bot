from config import bot, ADMIN_ID
from aiogram import types, Dispatcher
import datetime
from database.sql_commands import DataBase


async def message_ban(message: types.Message):
    ban_words = ['fuck', 'bitch', 'damn']

    if message.chat.id == ADMIN_ID:
        for word in ban_words:
            if word in message.text.lower().replace(' ', ""):
                ban_user = DataBase().sql_select_ban_users_command(
                    telegram_id=message.from_user.id,
                )
                if ban_user and ban_user[0]['count'] >= 3:
                    await bot.send_message(
                        chat_id=message.from_user.id,
                        text='You were banned for 2 minutes because you cursed a lot'
                    )
                    await bot.ban_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.from_user.id,
                        until_date=datetime.datetime.now() + datetime.timedelta(minutes=2)
                    )

                elif ban_user:
                    print(ban_user)
                    DataBase().sql_update_count_ban_users_command(
                        telegram_id=message.from_user.id
                    )
                else:
                    DataBase().sql_insert_ban_users_command(
                        telegram_id=message.from_user.id
                    )
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )

                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Hey,{message.from_user.username}, no need to swear, otherwise I'll ban you forever"
                )


def register_chat_actions_handler(dp: Dispatcher):
    dp.register_message_handler(message_ban)