from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram import types

from keyboards.default import set_data_keyboard, menu_keyboard


@dp.message_handler(text='Change data', state='full_access')
async def change_the_sending_frequency(message: types.Message, state: FSMContext):
    await state.set_state('set_data')
    await message.answer(text='What would you like to change?', reply_markup=set_data_keyboard)


@dp.message_handler(text='Information', state='full_access')
async def change_the_sending_frequency(message: types.Message):
    await message.answer(text='Information', reply_markup=menu_keyboard)


@dp.message_handler(text='Future updates', state='full_access')
async def change_the_sending_frequency(message: types.Message):
    await message.answer(text='Future updates', reply_markup=menu_keyboard)
