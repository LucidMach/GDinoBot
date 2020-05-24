from pil import ImageOps,ImageGrab
import pyautogui as pg
import time
import numpy as np
import webbrowser

class Bot:
    def __init__(self):
        self.dinoCor = (174,620 )
        self.detectAreaDown = (self.dinoCor[0] + 120, self.dinoCor[1], self.dinoCor[0] + 220, self.dinoCor[1] + 5)
        self.detectAreaUp = (self.dinoCor[0] + 120, self.dinoCor[1] - 100, self.dinoCor[0] + 220, self.dinoCor[1] + 5 - 100)
       
    def  start(self):
        pg.hotkey("space")
      
    def jump(self):
        pg.hotkey("Space") 

    def stayLow(self):
        pg.hotkey("down")

    def detection(self):
        imageDown = ImageGrab.grab(self.detectAreaDown)
        grayImgDown = ImageOps.grayscale(imageDown) 
        arrDown = np.array(grayImgDown.getcolors())

        imageUp = ImageGrab.grab(self.detectAreaUp)
        grayImgUp = ImageOps.grayscale(imageUp) 
        arrUp = np.array(grayImgUp.getcolors())

        return arrDown.mean(),arrUp.mean()

    def main(self):
        self.start()
        upDet, downDet = self.detection()
        while True: 
            if downDet < 273:
                self.jump()
            elif upDet < 273:
                self.stayLow()
                            

webbrowser.open("http://www.trex-game.skipser.com/")
pg.hotkey("win","left")
bot = Bot()
bot.main() 
