from aiogram import types
from loader import dp
from random import *



@dp.message_handler(commands=['start','старт'])
async def mes_start(message: types.Message):
    await message.answer(f'Бот-синоптик приветствует Вас!\n'
                         f'Выберите интересующий параметр\n'
                         f'1 - температура\n'
                         f'2 - скорость ветра\n'
                         f'3 - осадки\n')
    
@dp.message_handler(commands=['1'])
async def mes_help(message: types.Message):
    temp = choice (range(-20, 0))
    await message.answer(f'Температура окружающей среды  {temp} гр С')   


@dp.message_handler(commands=['2'])
async def mes_help(message: types.Message):
    speed = choice(range(0, 20))
    await message.answer(f'Скорость ветра  {speed} м/с')

@dp.message_handler(commands=['3'])
async def mes_help(message: types.Message):
    prec = choice(range(2))
    if prec == 0:
        await message.answer(f'Идет снег')
    else:
            await message.answer(f'Без осадков')    

