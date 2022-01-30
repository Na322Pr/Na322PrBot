from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Change data')
    ],
    [
        KeyboardButton(text='Information'),
    ],
    [
        KeyboardButton(text='Future updates'),
    ]
], resize_keyboard=True, one_time_keyboard=True)

set_data_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Change the sending frequency')
    ],
    [
        KeyboardButton(text='Change the selected arcana'),
    ]
], resize_keyboard=True, one_time_keyboard=True)
