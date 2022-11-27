from aiogram import types, Dispatcher
from create_bot import dp, bot

import db


async def commend_start(message: types.Message):
	"""
	Запуск бота
	"""
	await bot.send_message(message.from_user.id, 'Bot started')
	db.users_crud.add_user(message)
	await message.delete()
 
 
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commend_start, commands=['Start'])