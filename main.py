import asyncio
import logging
import os
import datetime
import requests
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command

from pathlib import Path
from dotenv import load_dotenv

language = 'ru_RU'

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
TG_URL = os.getenv('TG_URL')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()


@dp.message.handler(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку "
                        "погоды")


@dp.message_handler(Command(None))
async def get_weather(message: types.Message):
    pass


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
