from widgets.ui_register import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow


class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login)

    def register(self):
        ...
    def goLogin(self):
        ...
