# week9-1-pyqt-notes.py
import sys
# excecute os commands
frmo PyQt5.QtWidgets import QApplication, QWidget, QLineExit, QPushButton,QAction,QMessageBox,QMainWindow
from PyQt5.QtGui import QApplication
from PyQt5.QtCore import pyqtSlot
class App(QtWidget):
    def __init__(self):
        super().__init__()
        self.title = 'simple'
        self.left = 20
        self.top = 20
        self.width = 600
        self.height = 500
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.textbox = QLineExit(self)
        self.textbox.move(30,30)
        self.textbox.resize(250,40)

        self.button = QPushButton('Show Text', self)
        self.button.move(30,60)
        self.button.clicked.connect(self.on_click)

        self.show()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('file')
        edit_menu = main_menu.addMenu('edit')
        view_menu = main_menu.addMenu('view')

        exit_button = QAction(QIcon('exit24.png'),'exit',self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip("exit")
        exit_button.triggered.connect(self.close)

    @pyqtSlot()
    def on_click(self):
        textbox_value = self.textbox.text()
        QMessageBox.question(self, "message","typed{}".format(textbox_value),
                                QMessageBox.Ok,QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
