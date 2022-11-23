from aiogram import types,Dispatcher
from create_bot import bot
from Buttons import btn_user
from DataBase import sqlite_db
import sys


async def command_start(message : types.Message):
    await bot.send_photo(message.from_user.id,"https://sun9-west.userapi.com/sun9-50/s/v1/ig2/AYSV5QL5QOg4ztasA7mK0P4_ZhDaptpLdPkGeYPhPLH9ICpGzapuAnhUeNWJXlRJhUlNNDBFv-WAwDCeu-2-GBSz.jpg?size=796x661&quality=96&type=album")
    await bot.send_message(message.from_user.id, 'Здравствуйте. Я бот созданный для показа товаров нашего магазина.\nВоспользуйтесь кнопками телеграмма, для просмотра информации магазина.', reply_markup=btn_user)

async def command_location(message: types.Message):
    await bot.send_photo(message.from_user.id,"https://sun9-west.userapi.com/sun9-4/s/v1/ig2/Cb0v1994AV-o0pObZ265FwJzTk6Q1Mu_3bqDrf0NYKWS2C59cKgRqeEe_ys7RVKr3H8e7mJ9SAgLs7lBo7Yj6ax-.jpg?size=948x469&quality=96&type=album")
    await bot.send_message(message.from_user.id,'Адресс: Большой проспект П.С., 73 ​Каменноостровский проспект, 36 Кронверкское, Петроградский район, Санкт-Петербург')

async def command_contact_inform(message: types.Message):
    await bot.send_message(message.from_user.id,'Контакты для связи с магазином:\n+7(499)686-05-91 ФИО: Илья Иванович\n+7(499)686-05-92 ФИО: Александра Дмитриевна')

async def command_products(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_user(dp : Dispatcher):#для многоуровнего файла(Декораторы не используем@)
    dp.register_message_handler(command_start,commands=['start'])
    dp.register_message_handler(command_products, commands=['Товары'])
    dp.register_message_handler(command_contact_inform, commands=['Контакты'])
    dp.register_message_handler(command_location, commands=['Местоположение'])