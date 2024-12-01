import sys

from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow


class GitAndYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.button_clicked)
        canvas = QtGui.QPixmap(781, 681)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)

    def button_clicked(self):
        from random import randrange
        canvas = self.label.pixmap()
        canvas.fill(Qt.GlobalColor.white)
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(255, 255, 0))
        painter.setPen(pen)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(255, 255, 0))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)

        painter.drawEllipse(20, 70, int(randrange(22, 700)), int(randrange(102, 540)))
        painter.end()
        self.label.setPixmap(canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitAndYellowCircles()
    ex.show()
    sys.exit(app.exec())
