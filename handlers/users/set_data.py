from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram import types

from keyboards.default import time_pick_keyboard, hero_pick_keyboard, menu_keyboard
from data.temporary_database import one_hour, three_hour, six_hour, twelve_hour, one_day, two_day, arcanas
from utils.misc import set_frequency


@dp.message_handler(text='Change the sending frequency', state='set_data')
async def change_the_sending_frequency(message: types.Message, state: FSMContext):
    await message.answer(text='Select the sending frequency', reply_markup=time_pick_keyboard)
    await state.set_state('set_time')


@dp.message_handler(Text(equals=['1 hour', '3 hour', '6 hour', '12 hour', '1 day', '2 day']), state='set_time')
async def set_time(message: types.Message, state: FSMContext):
    user = message.from_user.id
    answer = message.text

    set_frequency(answer, user)
    await message.answer('Information saved', reply_markup=menu_keyboard)
    await state.set_state('menu')


@dp.message_handler(text='Change the selected arcana', state='set_data')
async def change_the_selected_arcana(message: types.Message, state: FSMContext):
    await message.answer(
        f"Selected characters:\n{', '.join(arcanas[message.from_user.id])}\nChoose the arcana you are interested in",
        reply_markup=hero_pick_keyboard)
    await state.set_state('set_hero')


@dp.message_handler(Text(
    equals=['Ogre Magi', 'Pudge', 'Rubick', 'Juggernaut', 'Monkey King', 'Zeus', 'Crystal Maiden', 'Phantom Assassin',
            'Shadow Fiend', 'Techies', 'Terrorblade', 'Legion Commander', 'Lina']), state='set_hero')
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
    await state.set_state('menu')
