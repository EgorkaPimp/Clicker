import pygetwindow as gw
from repiter import main


# Выводит название всех открытых вкладок
def windooow():
    windows = gw.getAllTitles()
    for title in windows:
        print(title)
    return windows


# Открытие окна во весь экран, запуск кликера
def activ_window(name):
    window = gw.getWindowsWithTitle(name)[0]
    window.activate()
    window.maximize()
    main()
    return
