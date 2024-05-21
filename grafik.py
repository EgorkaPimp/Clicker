import tkinter
from tkinter import *
import work_with_window
import work_sql
import read_db

radiobuttons = []

# Открытие окна
window = tkinter.Tk()
window.title("Clicker by Egorka")

# Размер окна
window.geometry('400x600')


# Функция запускает тестирование
def start_test():
    selected_value = var.get()
    print(f'Выбранная радиокнопка: {selected_value}')
    work_with_window.activate_window(selected_value)   # Передаем название окна в файл для работы с окнами
    return


# Передача название в БД
def testing():
    selected_value = var.get()
    print(selected_value)
    read_db.name_sc_db(selected_value)
    return


# Очиста радиокнопок
def clear_radiobuttons():
    """Функция для очистки всех радиокнопок"""
    for rb in radiobuttons:
        rb.destroy()
    radiobuttons.clear()


# Выполняет поиск открытых вкладок
def search_window():
    clear_radiobuttons()

    win = work_with_window.search_windows()
    ar = []
    for i in win:
        if len(i) > 1:
            ar.append(i)

    # Создаем и размещаем радиокнопки
    for value in set(ar):
        radio_button = Radiobutton(window, text=value, variable=var, value=value)
        radio_button.pack(anchor='sw')
        radiobuttons.append(radio_button)
    return


# Выполняет поиск открытых вкладок
def redy_test():
    clear_radiobuttons()

    # Создаем и размещаем радиокнопки
    for value in set(read_db.name_test_db()):
        radio_button = Radiobutton(window, text=value, variable=var, value=value)
        radio_button.pack(anchor='sw')
        radiobuttons.append(radio_button)
    return


# Создаем название теста
def create_name_test():
    global entered_text
    entered_text = text_entry.get()  # Получаем текст из поля ввода
    print(f'Введенный текст: {entered_text}')
    text_name = Label(window, text=f'Название теста: {entered_text}')
    text_name.place(x=130, y=3)
    work_sql.name_test(entered_text)   # Передаем название в функцию хранения имени теста
    text_entry.delete(0, tkinter.END)


var = StringVar()
# Создание кнопок
text_entry = Entry(window)
text_entry.pack(anchor='sw')   # Область ввода названия
bt_entry = Button(window, text="Название", command=create_name_test)
bt_entry.pack(anchor='sw')   # Кнопка сохраняющая название
bt_search = Button(window, text="Определить окна", command=search_window)
bt_search.pack(anchor='se')   # Кнопка пояска открытых окон
bt_test = Button(window, text="Старт записи", command=start_test)
bt_test.pack(anchor='sw')   # Кнопка запуска тетста
bt_redy = Button(window, text="Готовые", command=redy_test)
bt_redy.pack(anchor='se')   # Кнопка вывода созданных тестов
bt_test = Button(window, text="Старт теста", command=testing)
bt_test.pack(anchor='sw')   # Кнопка запуска тетста


# Запуск приложения
window.mainloop()
