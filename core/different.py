from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State


class StaffStates(StatesGroup):
    fioState = State()
    postState = State()
    remarkState = State()


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('Добавить сотрудника', callback_data='add_user'))
    keyboard.row(types.InlineKeyboardButton('Сделать замечание', callback_data='remark'))
    keyboard.row(types.InlineKeyboardButton('Создать заявления', callback_data='create_statements'))
    return keyboard


statements_templates = {'REMARK': 'core/static/приказ.docx',
                        'REPRIMAND': 'core/static/Шаблон выговор.docx',
                        'DISMISSAL': 'core/static/Шаблон приказа увольнения.docx'}
