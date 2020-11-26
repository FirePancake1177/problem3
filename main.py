import sys
import random as rand
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.run)
        self.start = False

    def run(self):
        self.start = True
        self.repaint()

    def paintEvent(self, event):
        if self.start:
            painter = QPainter()
            painter.begin(self)
            self.draw(painter)
            painter.end()

    def draw(self, painter):
        painter.setBrush(QColor(255, 255, 0))
        for i in range(rand.randint(1, 10)):
            size = rand.randint(10, 100)
            x, y = rand.randint(50, 400), rand.randint(160, 350)
            painter.drawEllipse(x, y, size, size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
