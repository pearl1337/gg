from PyQt5 import Qt

import requests

class LoadUrlThread_Post(Qt.QThread):
    load_finished = Qt.pyqtSignal(object)

    def __init__(self, url, body):
        super().__init__()

        self.url = url

        self.body = body

    def run(self):
        
        rs = requests.post(self.url,self.body)

        self.load_finished.emit(rs)