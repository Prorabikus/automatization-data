from aiogram import types
from aiogram.dispatcher import FSMContext
from config import db
from core.different import StaffStates


async def remark(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(StaffStates.remarkState)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for user in db.get_users().values():
        keyboard.insert(types.InlineKeyboardButton(user['fio'], callback_data=user['id']))
    await call.message.answer('Выберите сотрудника', reply_markup=keyboard)
    await call.answer()


async def get_user(call: types.CallbackQuery, state: FSMContext):
    user = db.get_users().get(int(call.data))
    user['remarks'] += 1
    db.add_remark(user['id'])

    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('Ок', callback_data='start'))
    await call.message.answer(f'Сотрудник получил {user["remarks"]} замечание', reply_markup=keyboard)
    await call.answer()
