from dataclasses import dataclass 
from config import TOKEN    
from aiogram import Bot, Dispatcher 
from aiogram.types import Message
from aiogram.filters import Command


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def start_message(message: Message) -> None:
    await message.answer(
        text='Hi'
    )


async def message_filter(message: Message) -> None:
    await message.answer(
        text='Простые сообщения'
    ) 


dp.message.register(start_message, Command(commands=['start']))
dp.message.register(message_filter)


if __name__ == "__main__":
    dp.run_polling(
       bot
    )

