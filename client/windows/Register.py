
# from widgets.ui_register import Ui_RegisterWindow
from PyQt5.QtWidgets import  QMainWindow, QPushButton
class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__()
        self.setWindowTitle('Window1')
        self.setMinimumWidth(200)
        self.setMinimumHeight(50)
        self.button = QPushButton(self)
        self.button.setText('Ok')
        self.button.show()
