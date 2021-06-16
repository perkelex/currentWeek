from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import datetime

class PicGenerator:
    def __init__(self):
        pass

    def generatePic(self, text):
        img = Image.new('RGB', (256, 256), color = (1, 1, 1))

        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('arial.ttf', 230)
        d.text((0,0), str(text), font=fnt, fill=(255,255,255))

        img.save('icon.ico')

class TrayInfo:
    def __init__(self, year, week, day):
        super().__init__()
        self.year = year
        self.week = week
        self.day = day
        self.cwText = f"CW {self.week}"
        self.menu_options = ((self.cwText, None, self.showCurrentWeek),)
        self.systray = SysTrayIcon("icon.ico", self.cwText, self.menu_options)

    def showCurrentWeek(self, systray):
        print(self.cwText)

    def show(self):
        self.systray.start()
        self.setDate()

    def setDate(self):
        self.year, self.week, self.day = datetime.date.today().isocalendar()


if __name__ == "__main__":
    year, week, day = datetime.date.today().isocalendar()

    pg = PicGenerator()
    pg.generatePic(week)

    tray = TrayInfo(year, week, day)
    tray.show()