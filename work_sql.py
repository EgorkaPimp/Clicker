import sqlite3
import repiter

n_test = 'test'
n_window = 'Not data'


# Функция хранения имени выброного окна
def name_window(name_w):
    global n_window
    n_window = name_w


# Функция хранения название теста
def name_test(name_t):
    global n_test
    n_test = name_t


# Создание и заполнение базы данных
def db_work():
    # Подключение к базе данных
    con = sqlite3.connect('db/database.db')
    cursor = con.cursor()

    # Получение массива из функции
    coordinate = repiter.giv_to_db()
    print(f'save array {coordinate}')

    # Создание таблици, если не создана
    cursor.execute("""CREATE TABLE IF NOT EXISTS baza (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    name_window TEXT NOT NULL,
    array TEXT NOT NULL)""")

    # Добавление данных в таблицу
    cursor.execute(f""" INSERT INTO baza 
    (name, name_window, array) 
    VALUES ("{n_test}", "{n_window}", "{coordinate}")""")

    # Сохранение и закрытие
    con.commit()
    con.close()
