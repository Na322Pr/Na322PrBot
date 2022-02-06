from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram import types

from keyboards.default import time_pick_keyboard, hero_pick_keyboard, menu_keyboard
from data.temporary_database import one_hour, three_hour, six_hour, twelve_hour, one_day, two_day, arcanas


@dp.message_handler(text='Change the sending frequency', state='set_data')
async def change_the_sending_frequency(message: types.Message, state: FSMContext):
    await message.answer(text='Select the sending frequency', reply_markup=time_pick_keyboard)
    await state.set_state('set_time')


@dp.message_handler(Text(equals=['1 hour',
                                 '3 hour',
                                 '6 hour',
                                 '12 hour',
                                 '1 day',
                                 '2 day']), state='set_time')
async def set_time(message: types.Message, state: FSMContext):
    user = message.from_user.id
    answer = message.text

    if user in one_hour:
        one_hour.remove(user)
    if user in three_hour:
        three_hour.remove(user)
    if user in six_hour:
        six_hour.remove(user)
    if user in twelve_hour:
        twelve_hour.remove(user)
    if user in one_day:
        one_day.remove(user)
    if user in two_day:
        two_day.remove(user)

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
    await message.answer('Information saved', reply_markup=menu_keyboard)
    await state.set_state('full_access')


@dp.message_handler(text='Change the selected arcana', state='set_data')
async def change_the_selected_arcana(message: types.Message, state: FSMContext):
    await message.answer(
        f"Selected characters:\n{', '.join(arcanas[message.from_user.id])}\nChoose the arcana you are interested in",
        reply_markup=hero_pick_keyboard)
    await state.set_state('set_hero')


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
                                 'Lina']), state='set_hero')
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


@dp.message_handler(text='Закончить', state='set_hero')
async def answer_q1(message: types.Message, state: FSMContext):
    await message.answer('Information saved', reply_markup=menu_keyboard)
    await state.set_state('full_access')
