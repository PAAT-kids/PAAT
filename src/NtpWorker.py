from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from autoNTP import startNTPAuto, startSsdpGA

class WorkerThreadNTP(QThread):
    update_progress = pyqtSignal(str)

    def __init__(self, source, dst):
        super(QThread, self).__init__()
        self.source = source
        self.dst = dst

    def run(self):
        if self.source:
            self.update_progress.emit("<h1>NTP</h1>NTP Random Selection Has Started")
            result = startNTPAuto(self.source,self.dst)
            self.update_progress.emit(result)
        else:
            self.update_progress.emit('<div> <h1>Error</h1>' +'<p> No source Address specified! </p>'+'</div>')
           