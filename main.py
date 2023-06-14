from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import token
import logging

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

keyboard_buttons = [
    KeyboardButton('/start'),
    KeyboardButton('/help'),
    KeyboardButton('/backend'),
    KeyboardButton('/frontend'),
    KeyboardButton('/uxui'),
    KeyboardButton('/android'),
    KeyboardButton('/ios')

]
keyboard_one = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=30).add(*keyboard_buttons)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.",  reply_markup=keyboard_one)

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу помочь?")

@dp.message_handler(commands='backend')
async def backend(message:types.Message):
    await message.answer("Backend-разработчик – это программист, который создает и поддерживает нужные механизмы, они, в свою очередь, обрабатывают данные и выполняют определенные действия на сайтах. Такой разработчик участвует в хранении данных, безопасности, архитектуре и других серверных функциях, которые не видит обычный пользователь..\nСтоимость курса: 10000 сом в месяц.\nОбучение: 5 месяцев.")

@dp.message_handler(commands='frontend')
async def frontend(message:types.Message):
    await message.answer("Frontend-разработчик — это специалист, который занимается разработкой пользовательского интерфейса, то есть той части сайта или приложения, которую видят посетители страницы. Главная задача фронтенд разработчика — перевести готовый дизайн-макет в код так, чтобы все работало правильно.\nСтоимость курса: 10000 сом в месяц.\nОбучение: 5 месяцев.")

@dp.message_handler(commands='uxui')
async def uxui(message:types.Message):
    await message.answer("UX/UI-дизайн — это проектирование удобных, понятных и эстетичных пользовательских интерфейсов.\nСтоимость курса: 10000 сом в месяц.\nОбучение: 5 месяцев")

@dp.message_handler(commands='android')
async def android(message:types.Message):
    await message.answer("Android-разработчик создает приложения для устройств на операционной системе Android. Он пишет код, работает над интерфейсом и дизайном, тестирует приложение и исправляет баги, а также адаптирует его под разные модели устройств (которых у Android великое множество).\nСтоимость курса: 10000 сом в месяц\nОбучение: 5 месяцев")

@dp.message_handler(commands='ios')
async def ios(message:types.Message):
    await message.answer("iOS-разработчик, или iOS developer, — это программист, который пишет сервисы и программы для айфонов. Из-за особенностей устройств Apple и их операционной системы для них нужно писать специальный код. Основной язык, на котором пишут код iOS-разработчики, — Swift..\nСтоимость курса: 10000 сом в месяц.\nОбучение: 5 месяцев.")

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)