from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()#Место хранения - оперативная память

bot=Bot(token="5834836107:AAFDnRI_mqW52_zDDSIDhQqJoTb55T78SeE")
dp=Dispatcher(bot, storage=storage)