import requests
import telebot
import os
from pathlib import Path
from dotenv import load_dotenv
from telebot.apihelper import ApiException

language = 'ru_RU'

BASE_DIR = Path(__file__).resolve().parent

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
API_KEY_WEATHER = os.getenv('API_KEY_WEATHER')

start_text = ("Привет! Это бот для погоды в городе.\n"
              "Создан в качестве теста для компании BobrAi.\n"
              "Введите /weather <город>.")

bot = telebot.TeleBot(TG_BOT_TOKEN)


def generate_result(data, city):
    temp = int(data['list'][0]['main']['temp'])
    feels_like = data['list'][0]['main']['feels_like']
    pressure = int(data['list'][0]['main']['pressure']) * 0.75
    humidity = data['list'][0]['main']['humidity']
    wind_speed = int(data['list'][0]['wind']['speed'])
    rain = 'не ожидается' if data['list'][0]['rain'] is None else 'ожидается'
    snow = 'не ожидается' if data['list'][0]['snow'] is None else 'ожидается'
    weather = data['list'][0]['weather'][0]['description']
    return f'''
<b>Прогноз погоды в городе {city}</b>

Сейчас температура {temp}°C
Ощущается как {feels_like}°
⛅️{weather}⛅️
💨 Скорость ветра {wind_speed}м/с 💨
Давление {pressure} мм рт.ст.
Влажность {humidity}%
💦 Дождь {rain}
❄️ Снег {snow}
'''


def request_weather(city):
    result = requests.get("https://ru.api.openweathermap.org/data/2.5/find",
                          params={
                              'q': city,
                              'type': 'like',
                              'units': 'metric',
                              'lang': 'ru',
                              'APPID': API_KEY_WEATHER,
                          }).json()
    if result['cod'] != '200' or result['count'] == 0:
        return 0
    else:
        return generate_result(result, city)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_text, parse_mode='Markdown')


@bot.message_handler(commands=['weather'])
def get_weather(message):
    city = message.text.split()[1]
    bot.send_message(message.from_user.id, f'{city}')


def main():
    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    print(request_weather('Ковров'))
    # while True:
    #     try:
    #         main()
    #     except Exception as e:
    #         print(f'❌❌❌❌❌ Сработало исключение! {e} ❌❌❌❌❌')
