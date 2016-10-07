from PyQt4 import QtCore, QtGui, uic
import sys

servidor = uic.loadUiType("Snake_Servidor.ui")[0]

class Servidor_Uso(QtGui.QMainWindow, servidor):
	
	def __init__(self,parent = None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.resize(800,500)
		self.cuadricula()
		self.show()

	def cuadricula(self):
		self.tabla.horizontalHeader().setStretchLastSection(True)
		self.tabla.verticalHeader().setStretchLastSection(True)
		self.tabla.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.tabla.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

app = QtGui.QApplication(sys.argv)
c = Servidor_Uso()
sys.exit(app.exec_())

