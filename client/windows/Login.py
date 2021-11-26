from widgets.ui_mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow, QMessageBox

from server.urlThread import LoadUrlThread_Post


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.loginButton.clicked.connect(self.login)


    def on_finished_load_url(self, rs):
        self.setWindowTitle('After load: {}'.format(rs))    

    def login(self):

        login = self.ui.loginInput.text()

        password = self.ui.passwordInput.text()

        if len(login) > 3 or len(password) > 10:
            self.thread = LoadUrlThread_Post('http://localhost:3000/login', {
                "login": login,
                "password": password
            })
            self.thread.load_finished.connect(self.on_finished_load_url)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            error = QMessageBox()
            error.setText('Форма не прошла валидацию!')

            error.exec_()
        

        

     
