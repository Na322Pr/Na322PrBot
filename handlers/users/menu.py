from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram import types

from keyboards.default import set_data_keyboard, menu_keyboard, delete_data_keyboard


@dp.message_handler(text='Change data', state='full_access')
async def change_data(message: types.Message, state: FSMContext):
    await state.set_state('set_data')
    await message.answer(text='What would you like to change?', reply_markup=set_data_keyboard)


@dp.message_handler(text='Delete data', state='full_access')
async def get_over_me(message: types.Message, state: FSMContext):
    await state.set_state('delete_data')
    await message.answer(text='Are you sure?', reply_markup=delete_data_keyboard)


@dp.message_handler(text='Yes', state='delete_data')
async def get_over_me(message: types.Message, state: FSMContext):
    await state.set_state('delete_data')
    await state.finish()
    await message.answer(text='Your data has been deleted.\nIf you want to use the bot in the future, type /start')


@dp.message_handler(text='No', state='delete_data')
async def get_over_me(message: types.Message, state: FSMContext):
    await state.set_state('full_access')
    await message.answer(text="Okey", reply_markup=menu_keyboard)
