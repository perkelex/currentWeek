from infi.systray import SysTrayIcon
from time import sleep
import datetime

class TrayInfo:
    def __init__(self):
        super().__init__()
        self.year, self.week, self.day = datetime.date.today().isocalendar()
        self.cwText = f"CW {self.week}"
        self.menu_options = ((self.cwText, None, self.showCurrentWeek),)
        self.systray = SysTrayIcon("icon.ico", self.cwText, self.menu_options)

    def showCurrentWeek(self, systray):
        print(self.cwText)

    def show(self):
        self.systray.start()
        self.updateWeek(3600)

    def updateWeek(self, delay):
        while True:
            self.year, self.week, self.day = datetime.date.today().isocalendar()
            self.systray.update(hover_text=f"CW {self.week}")
            sleep(delay)
        
TrayInfo().show()
