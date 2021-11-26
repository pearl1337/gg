import sys

from PySide6.QtWidgets import QApplication
# from windows.Login import LoginWindow

from windows.main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.showLogin()
    
    sys.exit(app.exec_())
