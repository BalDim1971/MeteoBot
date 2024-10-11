"""
Функции получения данных о погоде с сайта OpenWeatherMap.org
"""

import requests
from src.service import API_KEY_WEATHER


def generate_result(data: dict, city: str) -> str:
    """
    Генерируем результат по данным о погоде.
    :param data: Данные о погоде json-формат.
    :param city: Город.
    :return: Строка с расшифровкой погоды.
    """
    temp = int(data['list'][0]['main']['temp'])
    feels_like = data['list'][0]['main']['feels_like']
    pressure = int(data['list'][0]['main']['pressure']) * 0.75
    humidity = data['list'][0]['main']['humidity']
    wind_speed = int(data['list'][0]['wind']['speed'])
    rain = 'не ожидается' if data['list'][0]['rain'] is None else 'ожидается'
    snow = 'не ожидается' if data['list'][0]['snow'] is None else 'ожидается'
    weather = data['list'][0]['weather'][0]['description']
    
    return f'''
Прогноз погоды в городе {city}

Сейчас температура {temp}°C
Ощущается как {feels_like}°
⛅️{weather}⛅️
💨 Скорость ветра {wind_speed}м/с 💨
Давление {pressure} мм рт.ст.
Влажность {humidity}%
💦 Дождь {rain}
❄️ Снег {snow}
'''


def request_weather(city: str) -> str:
    """
    Получение данных о погоде с сайта OpenWeatherMap.org по городу.
    :param city: Наименование города.
    :return: Строка с результатом. Если город отсутствует или ошибка -
    возвращается строка с описанием ошибки.
    """
    
    result = requests.get("https://ru.api.openweathermap.org/data/2.5/find",
                          params={
                              'q': city,
                              'type': 'like',
                              'units': 'metric',
                              'lang': 'ru',
                              'APPID': API_KEY_WEATHER,
                          }).json()
    if result['cod'] != '200':
        return f"Ошибка сервера {result['cod']} {result['message']}"
    elif result['count'] == 0:
        return f"Город '{city}' не найден"
    else:
        return generate_result(result, city)
