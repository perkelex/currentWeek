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
    def __init__(self):
        super().__init__()
        self.setStartupTime()
        self.setYWD()
        self.setCurrentWeekText()
        self.setMenuOptions()
        self.setSysTray()

    def show(self):
        self.systray.start()

    def dummyTrigger(self, systray):
        ''' Stand-in for on-click event trigger '''
        pass

    def setSysTray(self):
        self.systray = SysTrayIcon("icon.ico", self.cwText, self.menu_options)

    def setMenuOptions(self):
        self.menu_options = (
            (self.startupTime, None, self.dummyTrigger),
            (self.cwText, None, self.dummyTrigger),
        )

    def setCurrentWeekText(self):
        self.cwText = f"CW {self.week}"

    def setStartupTime(self):
        self.startupTime = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def setYWD(self):
        self.year, self.week, self.day = datetime.date.today().isocalendar()

    def getWeek(self):
        return self.week

if __name__ == "__main__":
    tray = TrayInfo()

    pg = PicGenerator()
    pg.generatePic(tray.getWeek())

    tray.show()