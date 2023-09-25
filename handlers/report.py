from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from database.sql_commands import DataBase


class ReportStates(StatesGroup):
    username = State()
    reason = State()


async def report_start_call(call: types.CallbackQuery):
    if call.message.chat.type == 'private':
        await bot.send_message(
            chat_id=call.message.chat.id,
            text='Пожалуйста, отправьте Username пользователя, на которого хотите пожаловаться'
        )
        await ReportStates.username.set()


async def load_username(message: types.Message, state: FSMContext):
    username = message.text
    users = DataBase().sql_select_users_report_command(
        username=username,
    )
    print(users)
    if not users:
        await bot.send_message(
            chat_id=message.chat.id,
            text='Введите корректное имя пользователя!(Снова нажмите на report)'
        )
        await state.finish()

    else:
        for user in users:
            telegram_id = user['telegram_id']
            async with state.proxy() as data:
                data['username'] = username
                data['telegram_id'] = telegram_id
            print(data)
            await state.update_data(username=username, telegram_id=telegram_id)
            await ReportStates.next()
            await message.reply(
                'Пожалуйста, отправьте причину жалобы'
            )


async def load_reason(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['reason'] = message.text
        await bot.send_message(
            # chat_id=data['telegram_id'],
            chat_id=ADMIN_ID,
            text=f'@{data["username"]} на вас пришла жалоба\n'
                 f'Жалоба - {message.text}'
        )
    print(data)
    await message.reply(
        'Ваша жалоба принята'
    )
    complain_users = DataBase().sql_select_complain_users_command()
    print("im here")
    async with state.proxy() as data:
        if not complain_users:
            DataBase().sql_insert_complain_users_command(
                telegram_id_comp_user=message.from_user.id,
                telegram_id_bad_user=data['telegram_id'],
                reason=data['reason']
            )
        elif complain_users[0]['count'] >= 3:
            await bot.send_message(
                chat_id=data['telegram_id'],
                text='Вы были забанены, по причине многочисленных жалоб'
            )
        # await bot.ban_chat_member(
        #     chat_id=message.chat.id,
        #     user_id=message.from_user.id,
        #     until_date=datetime.datetime.now() + datetime.timedelta(minutes=2)
        # )

        elif complain_users:
            print(complain_users)
            DataBase().sql_update_count_bad_users_command(
                telegram_id_bad_user=data['telegram_id'],
            )

        await state.finish()


def register_report_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(report_start_call,
                                       lambda call: call.data == "report_start")
    dp.register_message_handler(load_username, state=ReportStates.username,
                                content_types=['text'])
    dp.register_message_handler(load_reason, state=ReportStates.reason,
                                content_types=['text'])
