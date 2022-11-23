from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp,bot
from DataBase import sqlite_db
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID=None

class FSMAdmin(StatesGroup):
    photo = State()# Конкретное состояние бота
    name = State()
    description=State()
    price=State()
 
async def make_changes_command(message: types.Message):
     global ID
     ID= message.from_user.id
     await bot.send_message(message.from_user.id, 'Теперь вы администратор')
     await message.delete()
     
async def command_start(message : types.Message):
    if message.from_user.id==ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')
    
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy()as data:#Открываем словарь
        data['photo']=message.photo[0].file_id#Сохраняем в словарь (Автоматом закрывается). Картинка будет в дальнейшем работать по айди номеру
    await FSMAdmin.next()#ожидание для бота следующего ответа
    await message.reply("Теперь введи название")
    
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy()as data:#Открываем словарь
        data['name']=message.text#Сохраняем в словарь (Автоматом закрывается). Картинка будет в дальнейшем работать по айди номеру
    await FSMAdmin.next()#ожидание для бота следующего ответа
    await message.reply("Введи описание")
    
async def load_description(message: types.Message, state: FSMContext):#Принимаем третий ответ и пишем в словарь
    async with state.proxy()as data:#Открываем словарь
        data['description']=message.text#Сохраняем в словарь (Автоматом закрывается). Картинка будет в дальнейшем работать по айди номеру
    await FSMAdmin.next()#ожидание для бота следующего ответа
    await message.reply("Укажи цену")
    
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy()as data:#Открываем словарь
        data['price']=float (message.text)#Сохраняем в словарь (Автоматом закрывается). Картинка будет в дальнейшем работать по айди номеру
    await sqlite_db.sql_add_command(state)

    await state.finish()#Полностью выходит из машинного состояния и всё очищается

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ',''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ","")} удалена.', show_alert=True)

async def delete_item(message: types.Message):
    if message.from_user.id==ID:
        read= await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
            await bot.send_message(message.from_user.id,text = "@@@@", reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


async def cancel_handler(message : types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

def register_handlers_admin (dp: Dispatcher):
    dp.register_message_handler(command_start,commands='Загрузить', state=None)
    dp.register_message_handler(load_photo,content_types=['photo'],state = FSMAdmin.photo)
    dp.register_message_handler(load_name,state = FSMAdmin.name)
    dp.register_message_handler(load_description,state = FSMAdmin.description)
    dp.register_message_handler(load_price,state = FSMAdmin.price)
    dp.register_message_handler(cancel_handler,state = "*",commands='Отмена')
    dp.register_message_handler(cancel_handler,Text(equals='отмена', ignore_case=True), state = "*")
    dp.register_message_handler(make_changes_command,commands=['SetupMeHowAdministrator'])
    dp.register_message_handler(delete_item,commands=['Удалить'])