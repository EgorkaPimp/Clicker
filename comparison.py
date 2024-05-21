import os.path
import time
from PIL import ImageGrab

import pyautogui
import cv2
import numpy as np


# Полный цикл сравнения
def start_t(name_scrin, name_test):
    for i in name_scrin:
        # Функция обработки скриншота рабочего стола
        def capture_screenshot():
            global screenshot_np
            # Захват текущего скриншота рабочего стола
            screenshot = ImageGrab.grab()
            screenshot_np = np.array(screenshot)
            # Конвертация из RGB в BGR для OpenCV
            screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
            return screenshot_bgr

        #  Функция сравнения и обработки
        def find_subimage(small_path):
            # Чтение большого изображения и подизображения
            small_image = cv2.imread(small_path)

            # Проверка, что изображения загружены корректно
            if small_image is None:
                print("Ошибка загрузки изображений.")
                return

            # Преобразование изображений в градации серого
            big_gray = capture_screenshot()
            small_gray = cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)

            # Применение метода matchTemplate
            result = cv2.matchTemplate(big_gray, small_gray, cv2.TM_CCOEFF_NORMED)

            # Задаем порог для обнаружения совпадения
            threshold = 0.95
            loc = np.where(result > threshold)

            # Новый путь к папке для сохранения скриншота
            save_folder = f"D:\\Click\\{name_test}"

            # Если совпадения найдены, рисуем квадраты на большом изображении
            if len(loc[0]) > 0:
                print("Подизображение найдено.")
                for pt in zip(*loc[::-1]):
                    # Рассчитываем центр совпавшей области
                    center_x = pt[0] + ll.shape[1] // 2
                    center_y = pt[1] + ll.shape[0] // 2

                    # Нажатие мышью в центр совпавшей области
                    pyautogui.click(center_x, center_y)
                    cv2.rectangle(screenshot_np, pt, (pt[0] + small_gray.shape[1], pt[1] + small_gray.shape[0]),
                                  (0, 255, 0), 2)
                    save_path = os.path.join(save_folder, f"screenshot_after_click_{pt}.png")
                    cv2.imwrite(save_path, screenshot_np)
                    break
            else:
                print("Подизображение не найдено.")
            return True

        capture_screenshot()
        # Пути к изображениям
        small_image_path = f'D:\\Click\\{name_test}\\{i}'
        ll = cv2.imread(small_image_path)
        time.sleep(5)

        # Вызов функции для поиска подизображения
        find_subimage(small_image_path)
