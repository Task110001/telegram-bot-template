from aiogram.utils import executor
from core.config import Base, db, engine
from utils import to_json
from create_bot import dp

import db.users_crud
from handlers import client, admin, other


async def on_startup(_):
  Base.metadata.create_all(bind=engine)
  print('Bot online')


client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)