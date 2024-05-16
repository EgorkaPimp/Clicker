import tkinter
from tkinter import *
from work_with_window import windooow, activ_window

# Открытие окна
window = tkinter.Tk()
window.title("Clicker by Egorka")

# Размер окна
window.geometry('500x400')
window.minsize(500, 400)
window.maxsize(600, 500)


# Функция запускает тестирование
def test():
    selected_value = var.get()
    print(f'Выбранная радиокнопка: {selected_value}')
    activ_window(selected_value)
    return


# Выполняет поиск открытых вкладок
def click():
    win = windooow()
    ar = []
    for i in win:
        if len(i) > 2:
            ar.append(i)

    # Создаем и размещаем радиокнопки
    for value in set(ar):
        radio_button = Radiobutton(window, text=value, variable=var, value=value)
        radio_button.pack()
    return


var = StringVar()

# Создание кнопок
bt_search = Button(window, text="Определить окна", command=click)
bt_search.place(x=10, y=10)
bt_test = Button(window, text="start test", command=test)
bt_test.place(x=10, y=50)
bt_redy = Button(window, text="Готовые", command=test)
bt_redy.place(x=10, y=100)

# Запуск приложения
window.mainloop()
