from aiogram import types, Dispatcher


async def command_echo(message : types.message):
    await message.reply("Вы написали")
    
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_echo)