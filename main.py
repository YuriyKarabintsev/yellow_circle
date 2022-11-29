from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random

class Wind(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        n = random.randint(1, 10)
        for i in range(n):
            d = random.randint(20, 150)
            start_x = random.randint(10, 600)
            start_y = random.randint(10, 800)
            qp.setBrush(QColor("yellow"))
            qp.drawEllipse(start_x, start_y, d, d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Wind()
    w.show()
    sys.exit(app.exec())