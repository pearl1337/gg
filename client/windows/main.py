from PyQt5.QtWidgets import  QMainWindow
# from windows.Login import LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')
    # def showRegister():
    #     print('register')
    # def showLogin(self):
    #     self.loginWindow = LoginWindow()
    #     self.loginWindow.registerButton.clicked.connect(self.showRegister)
    #     self.loginWindow.show()