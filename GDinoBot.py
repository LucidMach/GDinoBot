import pyautogui as pg, time

white = (255, 255, 255)

pg.hotkey("win","2")
time.sleep(1)
pg.typewrite("a")
pg.hotkey("enter")
time.sleep(1)
pg.hotkey("space ")
while True:
    while pg.pixel(x=900, y=750) == white: 
        if pg.pixel(x=679, y=333) != white:
            pg.hotkey("space")
        elif pg.pixel(x=679, y=333) == white and pg.pixel(x=679, y=305) != white:
            pg.keyDown("down")
            time.sleep(0.75)
            pg.keyUp("down")

    while pg.pixel(x=900, y=750) != white:
        if pg.pixel(x=679, y=333) == white:
            pg.hotkey("space")
        elif pg.pixel(x=679, y=333) != white and pg.pixel(x=679, y=305) == white:
            pg.keyDown("down")
            time.sleep(0.75)
            pg.keyUp("down")
