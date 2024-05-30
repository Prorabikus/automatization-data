
from aiogram import types
from aiogram.dispatcher import FSMContext
from config import db
from core.different import StaffStates


async def add_user(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(StaffStates.fioState)
    await call.message.answer('Введите ФИО сотрудника')
    await call.answer()


async def get_fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await state.set_state(StaffStates.postState)
    await message.answer('Введите должность сотрудника')


async def get_post(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    db.add_user(state_data.get('fio', ''), message.text)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('Ок', callback_data='start'))
    await message.answer('Сотрудник добавлен', reply_markup=keyboard)
