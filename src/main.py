################################################################################
## Project P.A.A.T.
## Created: 21/09/2021 By: Meenrit
## Last Edited:
## Purpose: Main file for ui code
################################################################################

################################################################################
## IMPORTS
################################################################################
import sys
import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import source_rc

################################################################################
## IMPORT GUI file
from login_su import *
################################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#######################################################################
		# SHOW WINDOW
		#######################################################################
		self.show()
		

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
	app = QApplication(sys.argv)
	########################################################################
	##
	########################################################################
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
########################################################################
## END===>
########################################################################