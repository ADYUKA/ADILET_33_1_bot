from aiogram import executor
from config import dp
from handlers import start, callback, chat_actions, fsm_form, report, reference
from database import sql_commands


async def onstart_up(_):
    db = sql_commands.DataBase()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
callback.register_callback_handlers(dp=dp)
report.register_report_handlers(dp=dp)
fsm_form.register_fsm_form_handlers(dp=dp)
reference.register_reference_handler(dp=dp)
chat_actions.register_chat_actions_handler(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up

    )