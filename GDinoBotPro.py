from pil import ImageOps,ImageGrab
import pyautogui as pg
import time
import numpy as np
import webbrowser

class Bot:
    def __init__(self):
        self.dinoCor = (174,620 )
        self.detectArea = (self.dinoCor[0] + 120, self.dinoCor[1], self.dinoCor[0] + 220, self.dinoCor[1] + 5)
         
    def setDinoCoords(self, x, y):
        self.dinoCor = (x, y)
       
    def  start(self):
        pg.hotkey("space")
        pg.keyDown("down")
      
    def jump(self):
        pg.keyUp("down")
        pg.hotkey("Space") 

    def stayLow(self):
        pg.keyDown("down")
    def detection(self):
        image = ImageGrab.grab(self.detectArea)
        gray_img = ImageOps.grayscale(image) 
        arr = np.array(gray_img.getcolors())
        return arr.mean()

    def main(self):
        self.start()
        while True: 
            if self.detection() < 273:
                self.jump()
                time.sleep(0.5)
            else:
                self.stayLow()
                            

webbrowser.open("http://www.trex-game.skipser.com/")
pg.hotkey("win","left")
bot = Bot()
bot.main() 