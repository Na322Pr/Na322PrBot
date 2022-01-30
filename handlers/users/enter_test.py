from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from keyboards.default import time_pick_keyboard, hero_pick_keyboard, menu_keyboard
from loader import dp
from aiogram import types

from data.temporary_database import one_hour, three_hour, six_hour, twelve_hour, one_day, two_day, arcanas


@dp.message_handler(state='enter_test')
async def enter_test_q1(message: types.Message, state: FSMContext):
    arcanas[message.from_user.id] = []
    await message.answer("Choose the characters whose arcana you are interested in:", reply_markup=hero_pick_keyboard)
    await state.set_state('enter_test_q1')


@dp.message_handler(Text(equals=['Ogre Magi',
                                 'Pudge',
                                 'Rubick',
                                 'Juggernaut',
                                 'Monkey King',
                                 'Zeus',
                                 'Crystal Maiden',
                                 'Phantom Assassin',
                                 'Shadow Fiend',
                                 'Techies',
                                 'Terrorblade',
                                 'Legion Commander',
                                 'Lina']), state='enter_test_q1')
async def hero_pick(message: types.Message):
    text = str(message.text)
    user = message.from_user.id
    sup = arcanas[user]
    if text not in sup:
        sup.append(text)
    else:
        sup.remove(text)
    arcanas[user] = sup
    await message.answer(f"Selected characters:\n{', '.join(sup)}")


@dp.message_handler(text='Закончить', state='enter_test_q1')
async def answer_q1(message: types.Message, state: FSMContext):
    await message.answer("Choose how often you want to receive information.", reply_markup=time_pick_keyboard)
    await state.set_state('enter_test_q2')


@dp.message_handler(Text(equals=['1 hour',
                                 '3 hour',
                                 '6 hour',
                                 '12 hour',
                                 '1 day',
                                 '2 day']), state='enter_test_q2')
async def enter_test_q2(message: types.Message, state: FSMContext):
    answer = message.text

    if message.text == '1 hour':
        one_hour.append(message.from_user.id)
    if message.text == '3 hour':
        three_hour.append(message.from_user.id)
    if message.text == '6 hour':
        six_hour.append(message.from_user.id)
    if message.text == '12 hour':
        twelve_hour.append(message.from_user.id)
    if message.text == '1 day':
        one_day.append(message.from_user.id)
    if message.text == '2 day':
        two_day.append(message.from_user.id)

    print(arcanas, one_hour)
    await message.answer('Initial setup complete.\nNow you can:\nLearn information about this bot in Info\nsomething in help\nchange data', reply_markup=menu_keyboard)
    await state.set_state('full_access')
