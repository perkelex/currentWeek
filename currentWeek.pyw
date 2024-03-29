from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image, ImageDraw, ImageFont
from getpass import getuser
import sys
import datetime

PIC_NAME = "C:\\Users\\" + getuser() + "\\AppData\\Local\\Temp\\currentWeek_icon.ico"

class PicGenerator:
    def __init__(self):
        pass

    def generatePic(self, text):
        img = Image.new("RGB", (256, 256), color = (0, 0, 0))

        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("arial.ttf", 230)
        green = (0, 255, 0)
        if int(text) < 10:
            d.text((60,0), str(text), font=fnt, fill=green)
        else:
            d.text((0,0), str(text), font=fnt, fill=green)


        img.save(PIC_NAME)

class TrayInfo():
    def __init__(self, cw) -> None:
        super().__init__()
        self.app = QtWidgets.QApplication()
        self.cw = cw

        icon = QtGui.QIcon(PIC_NAME)
        menu = QtWidgets.QMenu()

        menu.addAction(self.getStartupTime())
        menu.addAction(f"CW {self.cw}")

        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(sys.exit)

        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip(f"CW {self.cw}")
        self.tray.show()

    def run(self):
        self.app.exec()

    def getStartupTime(self):
        return datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

if __name__ == "__main__":
    cw = datetime.date.today().isocalendar()[1]
    PicGenerator().generatePic(cw)
    TrayInfo(cw).run()