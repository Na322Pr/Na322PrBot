from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

okey_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Okey')
    ]
], resize_keyboard=True, one_time_keyboard=True)

