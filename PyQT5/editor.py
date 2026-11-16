from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QMenu, QMenuBar, QFileDialog, QAction

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Editor")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&File", self)
        self.menuBar.addMenu(fileMenu)

        # openFile = fileMenu.addMenu("&Open as...")
        # saveFile = fileMenu.addMenu("&Save as...")

        fileMenu.addAction("Open", self.action_clicked)
        fileMenu.addAction("Save as...", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            fname = QFileDialog.getOpenFileName(self, "Open File", "",)[0]
            try:
                with open(fname, "r") as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("File not found")
        elif action.text() == "Save as...":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                with open(fname, "w") as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("File not found")



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
