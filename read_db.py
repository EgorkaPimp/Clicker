import sqlite3
import json
import comparison


# Функция поиска названия скриншота в БД
def name_sc_db(a):
    print("Nachalo read db")
    con = sqlite3.connect('db/database.db')
    cursor = con.cursor()
    cursor.execute(f"""SELECT  name_scrin
                    FROM baza 
                    WHERE name = '{a}'""")
    mas = cursor.fetchall()
    z = json.dumps(mas[0])
    ttt = z.split("'")
    itog = []
    for i in ttt:
        if len(i) > 4:
            itog.append(i)
    name_test = f'{a}'
    con.close()
    # Запуск сравнения
    comparison.start_t(itog, name_test)
    print("Vse OK")
    return


# Функция поиска назавния теста из БД
def name_test_db():
    name_test = []
    con = sqlite3.connect('db/database.db')
    cursor = con.cursor()
    cursor.execute("""SELECT  name
                        FROM baza """)
    name = cursor.fetchall()
    con.close()
    z = json.dumps(name)
    tt = z.split('"')
    for i in tt:
        if len(i) > 4:
            name_test.append(i)
    return name_test
