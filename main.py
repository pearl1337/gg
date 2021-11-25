import sys

from PySide6.QtWidgets import QApplication
from windows.Login import LoginWindow

if __name__ == '__main__':
    app = QApplication()
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
