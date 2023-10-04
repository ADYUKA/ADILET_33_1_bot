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
    referral_button = InlineKeyboardButton(
        "REFERRAL MENU",
        callback_data="referral_menu"
    )
    news_button = InlineKeyboardButton(
        "5 Latest NEWS",
        callback_data="latest_news"
    )
    top_cartoons_button = InlineKeyboardButton(
        "TOP 5 CARTOONS",
        callback_data="top_cartoons"
    )
    markup.add(
        questionnaire_button
    ).add(
        form_start_button
    ).add(
        report_start_button
    ).add(
        referral_button
    ).add(
        news_button
    ).add(
        top_cartoons_button
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


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    generate_link_button = InlineKeyboardButton(
        "Generate Link 🔗",
        callback_data="generate_link"
    )
    referral_list_button = InlineKeyboardButton(
        "List of Referrals 📃",
        callback_data="referral_list"
    )
    markup.add(
        generate_link_button
    ).add(
        referral_list_button
    )
    return markup