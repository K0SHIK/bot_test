from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           Message)

BOT_TOKEN = '6914496241:AAHl9GHOPeyJblPhAhuuAqfQyujA181a1ao'
# Создаем бот и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
# Создаем объекты кнопок
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')
# Создаем объект клавиатуры
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])

# Хэндлер для команды старт
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего кошки больше боятся?',
        reply_markup=keyboard
    )

# Хэндлер будет срабатывать на ответ Собак и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно кошки бояться собак.'
             'Но вывидели как они бояться огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )

# Хэндлер будет срабатывать на ответ Огурцов и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки бояться больше',
        reply_markup=ReplyKeyboardRemove()
    )

if __name__ == '__main__':
    dp.run_polling(bot)
