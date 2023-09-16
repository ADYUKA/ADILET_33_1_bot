from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import DataBase
from keyboards.inline_buttons import question_first_keyboard


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


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(yes_answer_call,
                                       lambda call: call.data == "yes_answer")
    dp.register_callback_query_handler(no_answer_call,
                                       lambda call: call.data == "no_answer")