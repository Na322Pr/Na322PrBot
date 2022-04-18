from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import time_pick_keyboard, hero_pick_keyboard, okey_keyboard
from loader import dp



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await state.set_state('enter_test')
    await message.answer(f"Hi! Before using the bot, let's do the initial setup.", reply_markup=okey_keyboard)

