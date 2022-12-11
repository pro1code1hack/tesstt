"""
TT

1. Technology stack
2. Features
   1. Включать спотифай
   2. Выключать компьютер
   3. Скидать бабки на карточку
   4. Гуглить что-то
   5. Рандомную картинку с гугла
   6. Переводчик
   7. Погода
   8. Курс валют
   9. Включить камеру

Works
1- Даём команду --> она выполняется

TODO
1. Найти библиотеку для считывания голоса и перевода его в текст
2. Создать список команд
    [1] - Включить спотифай
    [2] - Выключить компьютер
    [3] - Скинуть деньги на карточку
    [4] - Гуглить что-то
    [5] - Рандомную картинку с гугла
    [6] - Переводчик
    [7] - Погода
    [8] - Курс валют
    [9] - Включить камеру

3. Создать функции для каждой команды


"""

from voice_handler import get_recognizer, record_audio, process_audio
from handlers import commands

recognizer = get_recognizer()
audio = record_audio(recognizer)
data = process_audio(recognizer, audio)

print(data)

commands[data]()

