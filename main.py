from aiogram.utils import executor
from create_bot import dp
from DataBase import sqlite_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()


from Handlers import user, admin,other

user.register_handlers_user(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)#старт бота