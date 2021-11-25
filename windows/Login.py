from widgets.ui_mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow

from windows.Register import RegisterWindow


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.register = RegisterWindow()
        
        self.ui.loginButton.clicked.connect(self.login)

        self.ui.registerButton.clicked.connect(self.goRegister)

        

    def login(self):
        text = self.ui.loginInput.text()
        print(text)

    def goRegister(self):
        self.hide()
        self.register.show()
