import asyncio
from aiogram import types
from core.different import statements_templates
from aiogram.types import InputFile
from config import db, bot
import docx


async def create_statements(call: types.CallbackQuery):
    all_statements = db.get_statements()
    n = len(all_statements)

    for user in db.get_users().values():
        user_statements = [s for s in all_statements if s['employee_id'] == user['id']]
        remarks = len([s for s in user_statements if s['type'] == 'REMARK'])
        reprimands = len([s for s in user_statements if s['type'] == 'REPRIMAND'])
        dismissal = len([s for s in user_statements if s['type'] == 'DISMISSAL'])

        if dismissal > 0:
            continue

        new_statement = {'REMARK': (user['remarks'] - remarks),
                         'REPRIMAND': min(3, user['remarks'] - 5) - reprimands,
                         'DISMISSAL': min(1, user['remarks'] - 8) - dismissal}

        for st_type, count in new_statement.items():
            for _ in range(count):
                doc = docx.Document(statements_templates[st_type])

                for paragraph in doc.paragraphs:
                    for run in paragraph.runs:
                        run.text = run.text.replace('NUM', str(n))
                        run.text = run.text.replace('FIO', user['fio'])
                        run.text = run.text.replace('POST', user['post'])

                doc.save('core/static/statement.docx')

                db.add_statements(user['id'], st_type)
                await bot.send_document(call.message.chat.id, InputFile('core/static/statement.docx'),
                                        caption=f'{user["fio"]}\n{st_type.lower()}')
                await asyncio.sleep(0.3)
                n += 1

    await call.answer()
