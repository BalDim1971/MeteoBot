"""
Сервисные функции и настроечные константы.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

language = 'ru_RU'

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
API_KEY_WEATHER = os.getenv('API_KEY_WEATHER')

START_TEXT = ("Привет! Это бот для погоды в городе.\n"
              "Создан в качестве теста для компании BobrAi.\n"
              "Введите /weather <город>.")
