from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image, ImageDraw, ImageFont
import sys
import datetime

PIC_NAME = "icon.ico"

class PicGenerator:
    def __init__(self):
        pass

    def generatePic(self, text):
        img = Image.new("RGB", (256, 256), color = (1, 1, 1))

        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("arial.ttf", 230)
        d.text((0,0), str(text), font=fnt, fill=(255,255,255))

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

    def generatePic(self):
        PicGenerator().generatePic(self.cw)

    def getStartupTime(self):
        return datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def getCurrentWeek(self):
        return datetime.date.today().isocalendar()[1]

if __name__ == "__main__":
    cw = datetime.date.today().isocalendar()[1]
    PicGenerator().generatePic(cw)
    TrayInfo(cw).run()