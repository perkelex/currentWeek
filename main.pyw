from infi.systray import SysTrayIcon
import datetime

class TrayInfo:
    def __init__(self):
        super().__init__()
        self.year, self.week, self.day = datetime.date.today().isocalendar()
        self.menu_options = (("Current Week", None, self.showCurrentWeek),)
        self.systray = SysTrayIcon("icon.ico", f"CW {self.week}", self.menu_options)

    def showCurrentWeek(self, systray):
        print(f"CW {self.week}")

    def show(self):
        self.systray.start()

tray = TrayInfo()
tray.show()
