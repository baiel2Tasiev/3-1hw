from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет, Выберите число от 1 до 3")

@dp.message_handler(text=["1", "2", "3"])
async def rand(message:types.Message):
    user = int(message.text)
    random_number = random.randint(1, 3)
    if random_number == user:
        await message.reply(f"Вы угадали! Правильный ответ: {random_number}")
    else:
        await message.answer(f"Вы не угадали. Правильный ответ: {random_number}")

executor.start_polling(dp)