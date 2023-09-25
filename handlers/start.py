from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot, ADMIN_ID, ADMIN_ID1, BOT_GIF
from const import START_TEXT
from database.sql_commands import DataBase
from keyboards.inline_buttons import start_keyboard


async def start_button(message: types.Message):
    print(message.get_full_command())
    command = message.get_full_command()

    if command[1]:
        print(command)
        existed_user = DataBase().sql_select_user_command(
            telegram_id=message.from_user.id
        )
        generate_link = await _create_link(link_type='start', payload=command[1])
        if not existed_user:
            owner = DataBase().sql_select_owner_by_link_command(
                link=generate_link
            )
            print(owner)
            DataBase().sql_insert_users_command(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
            )
            DataBase().sql_insert_reference_user_command(
                owner=owner[0]['telegram_id'],
                referral=message.from_user.id,
            )
    else:
        DataBase().sql_insert_users_command(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    print(message)
    with open(BOT_GIF, 'rb') as gif:
        await bot.send_animation(
            chat_id=message.chat.id,
            animation=gif,
            caption=START_TEXT.format(
                username=message.from_user.username
            ),
            parse_mode=types.ParseMode.MARKDOWN,
            reply_markup=await start_keyboard()
        )


async def secret_word(message: types.Message):
    if message.chat.id == ADMIN_ID or ADMIN_ID1:
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="'Secret information'"
        )
    else:
        # await bot.delete_message(
        #     chat_id=message.chat.id,
        #     message_id=message.message_id
        # )
        await bot.send_message(
            chat_id=message.chat.id,
            text="Hello my friend"
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_message_handler(secret_word, lambda word: "hello" in word.text)
