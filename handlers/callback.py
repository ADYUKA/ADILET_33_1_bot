from aiogram import types, Dispatcher
from config import bot
from const import PROFILE_CAPTION_TEXT
from database.sql_commands import DataBase
from keyboards.inline_buttons import question_first_keyboard
from scraper.new_scraper import NewScraper


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Did you eat today or Did you not eat today?",
        reply_markup=await question_first_keyboard()
    )


async def yes_answer_call(call: types.CallbackQuery):
    print(call)
    DataBase().sql_insert_answer_command(
        tg_id=call.from_user.id,
        username=call.from_user.username,
        first_answer="Yes"
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Cool, well done!",
    )


async def no_answer_call(call: types.CallbackQuery):
    print(call)
    DataBase().sql_insert_answer_command(
        tg_id=call.from_user.id,
        username=call.from_user.username,
        first_answer="No"
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Oh, hurry up and eat!",
    )


async def my_profile_call(call: types.CallbackQuery):
    print(call)
    user = DataBase().sql_select_user_form_command(
        telegram_id=call.from_user.id
    )
    with open(user[0]['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=PROFILE_CAPTION_TEXT.format(
                nickname=user[0]['nickname'],
                bio=user[0]['bio'],
                age=user[0]['age'],
                occupation=user[0]['occupation'],
                married=user[0]['married'],
            )
        )


async def latest_news_call(call: types.CallbackQuery):
    scraper = NewScraper()
    news = scraper.parse_data()

    for link in news:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=scraper.URL + link
        )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(yes_answer_call,
                                       lambda call: call.data == "yes_answer")
    dp.register_callback_query_handler(no_answer_call,
                                       lambda call: call.data == "no_answer")
    dp.register_callback_query_handler(my_profile_call,
                                       lambda call: call.data == "my_profile")
    dp.register_callback_query_handler(latest_news_call,
                                       lambda call: call.data == "latest_news")