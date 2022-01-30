from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

time_pick_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='1 hour'),
        KeyboardButton(text='3 hour'),
        KeyboardButton(text='6 hour'),
    ],
    [
        KeyboardButton(text='12 hour'),
        KeyboardButton(text='1 day'),
        KeyboardButton(text='2 day'),
    ]
], resize_keyboard=True, one_time_keyboard=True)
