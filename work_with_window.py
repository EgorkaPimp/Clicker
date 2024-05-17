import pygetwindow as gw
from repiter import start_listener
from work_sql import name_window


# Выводит название всех открытых вкладок
def search_windows():
    windows = gw.getAllTitles()
    for title in windows:
        print(title)
    return windows


# Открытие окна во весь экран, запуск кликера
def activate_window(name):
    window = gw.getWindowsWithTitle(name)[0]
    window.activate()
    window.maximize()
    name_window(name)
    start_listener()
    return
