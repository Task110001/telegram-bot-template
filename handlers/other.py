from aiogram import types, Dispatcher
from create_bot import dp, bot

import string
import json


async def echo_bot(message: types.Message):
  await bot.send_message(message.from_user.id, message.text)
  await message.delete()
      
      
def register_handlers_other(dp: Dispatcher):
  dp.register_message_handler(echo_bot)