from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Hello, world!")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Press me!")
        self.btn1.move(70, 150)
        self.btn1.setFixedWidth(200)
        self.btn1.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("New text added!")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()