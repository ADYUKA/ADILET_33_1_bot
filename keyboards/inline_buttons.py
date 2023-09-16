from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "START QUESTIONNAIRE",
        callback_data="start_questionnaire"
    )
    markup.add(
        questionnaire_button
    )
    return markup


async def question_first_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "YES😊)",
        callback_data="yes_answer"
    )
    no_button = InlineKeyboardButton(
        "NO😢",
        callback_data="no_answer"
    )
    markup.add(
        yes_button
    ).add(
        no_button
    )
    return markup