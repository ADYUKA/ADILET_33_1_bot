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
    form_start_button = InlineKeyboardButton(
        "REGISTRATION",
        callback_data="fsm_start"
    )
    report_start_button = InlineKeyboardButton(
        "REPORT",
        callback_data="report_start"
    )
    markup.add(
        questionnaire_button
    ).add(
        form_start_button
    ).add(
        report_start_button
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


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    profile_button = InlineKeyboardButton(
        "MY PROFILE",
        callback_data="my_profile"
    )

    markup.add(
        profile_button
    )
    return markup