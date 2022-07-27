# импортируем модули
import cv2
from mss.darwin import MSS as mss
import pyautogui as pag
import numpy as np
import time

# отчстёт времени
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

# создаём цикл
while True:
    # проверяем нажатие клавиши q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # получаем позицию курсора
    cursor_x, cursor_y = pag.position()

    # фотографируем область возле курсора
    mon = {'top': cursor_y-25, 'left': cursor_x-25, 'width': 50, 'height': 50}
    sct = mss()
    img = np.asarray(sct.grab(mon))

    # выводим картинку
    cv2.imshow('Bot\'s vision', img)

    # клик
    def click(timing):
        time.sleep(timing)
        pag.mouseDown(x=cursor_x, y=cursor_y, button='right')
        time.sleep(0.01)
        pag.mouseUp(x=cursor_x, y=cursor_y, button='right')

    # определяем цвет
    red_found = False
    for y in range(int(img.shape[0])):
        for x in range(int(img.shape[1])):
            b, g, r, a = img[y, x]
            if (r, g, b) == (211, 42, 42):
                if red_found == False:
                    red_found = True

    if red_found == False:
        # имитация клика
        click(1)
        click(1)