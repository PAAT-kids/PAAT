from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from ssdpAuto import startSsdpGA

class WorkerThread(QThread):
    update_progress = pyqtSignal(str)

    def __init__(self, source):
        super(QThread, self).__init__()
        self.source = source
        #self.chosen = chosenPkt

    def run(self):
        #if self.chosen == 'SSDP':
        if self.source:
            self.update_progress.emit("<h1>SSDP</h1>SSDP Random Selection Has Started")
            result = startSsdpGA(self.source)
            self.update_progress.emit(result)
        else:
            self.update_progress.emit('<div> <h1>Error</h1>' +'<p> No source Address specified! </p>'+'</div>')
           