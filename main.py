import telebot

from src.service import TG_BOT_TOKEN, START_TEXT
from src.weather import request_weather

bot = telebot.TeleBot(TG_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, START_TEXT, parse_mode='Markdown')


@bot.message_handler(commands=['weather'])
def get_weather(message):
    city = message.text.split()[1]
    result = request_weather(city)
    bot.send_message(message.from_user.id, f'{result}')


def main():
    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    # Добавить инициацию БД?
    while True:
        try:
            main()
        except Exception as e:
            print(f'❌❌❌❌❌ Сработало исключение! {e} ❌❌❌❌❌')
