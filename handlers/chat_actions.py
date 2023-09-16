from config import bot, ADMIN_ID
from aiogram import types, Dispatcher


async def message_ban(message: types.Message):
    ban_words = ['fuck', 'bitch', 'damn']

    if message.chat.id == ADMIN_ID:
        for word in ban_words:
            if word in message.text.lower().replace(' ', ""):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )

                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Hey,{message.from_user.username}, no need to swear, otherwise I'll ban you"
                )


def register_chat_actions_handler(dp: Dispatcher):
    dp.register_message_handler(message_ban)