
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from config import dp
from core.add_user import add_user, get_fio, get_post
from core.add_remark import remark, get_user
from core.different import StaffStates, main_keyboard
from core.statements import create_statements


async def start(message: types.Message):
    await message.answer('<b>Меню</b>', reply_markup=main_keyboard())


async def call_start(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('<b>Меню</b>', reply_markup=main_keyboard())
    await call.answer()


print('Старт')
if __name__ == "__main__":
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(call_start, text='start', state='*')
    dp.register_callback_query_handler(add_user, text='add_user')
    dp.register_message_handler(get_fio, state=StaffStates.fioState)
    dp.register_message_handler(get_post, state=StaffStates.postState)
    dp.register_callback_query_handler(remark, text='remark')
    dp.register_callback_query_handler(get_user, state=StaffStates.remarkState)
    dp.register_callback_query_handler(create_statements, text='create_statements')
    executor.start_polling(dp)
