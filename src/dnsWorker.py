from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from dnsAuto import startDNSAuto

class WorkerThreadDns(QThread):
    update_progress = pyqtSignal(str)

    def __init__(self, source, destination):
        super(QThread, self).__init__()
        self.source = source
        self.destination = destination
        #self.chosen = chosenPkt

    def run(self):
        if self.source:
            self.update_progress.emit("<h1>DNS</h1>DNS Random Selection Has Started")
            result = startDNSAuto(self.source, self.destination)
            self.update_progress.emit(result)
        else:
            self.update_progress.emit('<div> <h1>Error</h1>' +'<p> No source Address specified! </p>'+'</div>')
           