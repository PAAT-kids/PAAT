from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from ssdpAuto import startSsdpGA

class WorkerThread(QThread):
    def __init__(self,message):
        super(QThread, self).__init__()
        self.message = message
        #self.chosen = chosenPkt

    def run(self):
        #if self.chosen == 'SSDP':
        startSsdpGA(self.message)