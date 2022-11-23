from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b3 = KeyboardButton('/Товары')
b4 = KeyboardButton('/Контакты')
b5 = KeyboardButton('/Местоположение')

btn_user=ReplyKeyboardMarkup(resize_keyboard=True)#После использования кв, она скрывается

btn_user.add(b3).row(b4,b5)#.incert() добавляет кнопку меню сбоку. Тажке .Row(b1,b2)
