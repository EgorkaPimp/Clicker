import json

import work_sql

from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Controller as c_k
from pynput.mouse import Controller as c_m
from pynput.mouse import Button

kb = c_k()
ms = c_m()

# Масивы для записи координат и данных
ms_clicks_array = []
kb_clicks_array = []


# Функция воспроизведения записанных значений
def giv_to_db():
    a = json.dumps(ms_clicks_array)
    # a = 0
    # for i in ms_clicks_array:
    #     if isinstance(ms_clicks_array[a], list):
    #         ms.position = (ms_clicks_array[a])
    #         time.sleep(2)
    #         ms.click(Button.left)
    #         a += 1
    #     else:
    #         time.sleep(1)
    #         kb.press(ms_clicks_array[a])
    #         a += 1
    return a


# Функция записи нажатий мыши
def ms_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            coordinates = [x, y]
            ms_clicks_array.append(coordinates)
            print(ms_clicks_array)


# Функция записи нажатий клавиш
def kd_click(key):
    if key == keyboard.Key.esc:
        # Stop listener
        ms_listener.stop()
        work_sql.db_work()
        return False
    else:
        ms_clicks_array.append(key)
        print(ms_clicks_array)


# Запускается из "Работы с окнами"
def start_listener():
    global ms_listener
    # Передача данных в функции
    ms_listener = mouse.Listener(on_click=ms_click)
    kb_listener = keyboard.Listener(on_press=kd_click)

    # Запуск прослушивания
    kb_listener.start()
    ms_listener.start()

    # Ожидания конца прослушивания
    kb_listener.join()
    ms_listener.join()

    # Запуск репитора
    return
