#!usr/bin/python
# by Gabor Cristian
# Date: 02.03.2015
from __future__ import division
import sys
from PyQt4.QtGui import*
from PyQt4.QtCore import*

variabila=0.0
font=''' Acest program functioneaza pe baza licentei de libera distribuire. Sopul programului este unul, educativ. Programul calculeaza o formula numita: 'Legea Dilutiilor'. Se presupune ca se cunosc trei variabile, astfel incat programul va afisa rezultatul celei de-a patra variabile. In cazul in care se greseste la introducerea datelor, programul va recunoaste greseala si va afisa un mesaj de atentionare !   '''
txt="<font color='red'>Atentie!: Doar trei casute trebuiesc completate</font>"
avertizment="<font color='red'>Atentie!: Completeaza mai intai 3 casute</font>"
qt_app=QApplication(sys.argv)

class LayoutExample(QWidget):
	"""An example pf PySide/PyQt absolute positioning: the main window 
	   inherits from QWdiget a conveninet widget for an empty window"""

	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle('Legea Dilutiilor')
		self.setGeometry(100,100,400,400)

		# Setting the tab

		tab_widget=QTabWidget()
		self.tab1=QWidget(self)
		self.tab2=QWidget(self)

		# Creating the layouts for the QLineEdith and QLabel

		self.layout=QVBoxLayout(self.tab1)
		self.layout1=QGridLayout()
		self.button_box=QHBoxLayout()
		self.tabx=QVBoxLayout()


		tab_widget.addTab(self.tab1,"Formula")
		tab_widget.addTab(self.tab2,"Informatii")
		# Here we set the validator that allow to enter only numbers between 0 - 1000

		self.validator=QIntValidator(0,1000)


		# Setiing the Informatii tab
		self.inf_tab=QPlainTextEdit(self)
		self.inf_tab.setPlainText('%s' % font)
		self.tab2_layout=QVBoxLayout(self.tab2)
		self.tab2_layout.addWidget(self.inf_tab)

		# Setting the first Row With V1 and The QLineEdith for it
		self.var_1=QLineEdit(self)
		self.var_1.setMinimumWidth(100)
		self.var_1.setStyleSheet("QLineEdit { background: rgb(229,255,204); selection-background-color: rgb(233,99,0); }")
		self.var_1.setValidator(self.validator)
		self.var_1_name=QLabel('= V1',self)
		self.layout1.addWidget(self.var_1,0,0)
		self.layout1.addWidget(self.var_1_name,0,1)
			
		# Setting the second Row With C1 and The QLineEdith for it
		self.var_2=QLineEdit(self)
		self.var_2.setMinimumWidth(100)
  		self.var_2.setStyleSheet("QLineEdit { background: rgb(229,255,204); selection-background-color: rgb(233,99,0); }")
  		self.var_2.setValidator(self.validator)
  		self.var_2_name=QLabel('= C1', self)
  		self.layout1.addWidget(self.var_2,1,0)
  		self.layout1.addWidget(self.var_2_name,1,1)

  		# Setting the third Row With V2 and The QLineEdit for it

  		self.var_3=QLineEdit(self)
  		self.var_3.setMinimumWidth(100)
  		self.var_3.setStyleSheet("QLineEdit { background: rgb(229,255,204); selection-background-color: rgb(233,99,0); }")
  		self.var_3.setValidator(self.validator)
  		self.var_3_name=QLabel('= V2',self)
  		self.layout1.addWidget(self.var_3,2,0)
  		self.layout1.addWidget(self.var_3_name,2,1)

  		# Setting the fourth Row With C2 and The QLineEdit for it

  		self.var_4=QLineEdit(self) 
  		self.var_4.setMinimumWidth(100)
  		self.var_4.setStyleSheet("QLineEdit { background: rgb(229,255,204); selection-background-color: rgb(233,99.0); }")
		self.var_4.setValidator(self.validator)
		self.var_4_name=QLabel('= C2',self)
		self.layout1.addWidget(self.var_4,3,0)
		self.layout1.addWidget(self.var_4_name,3,1)


		# Setting the 
		# Setting the QLabel for the Result 
		self.result=QLabel('',self)
		self.layout1.addWidget(self.result,4,0)

		# Creating the button

		self.build_button=QPushButton('&Calculeaza',self)
		# Making the action and button layout

		self.build_button.clicked.connect(self.calculeaza_rezultatul)
		self.button_box.addWidget(self.build_button)
		self.button_box.addStretch(3)


		# Setting finaly layout arguments
		self.tabx.addWidget(tab_widget)	
		self.layout.addLayout(self.layout1)
		self.layout.addStretch(1)
		self.layout.addLayout(self.button_box)
		self.tabx.addLayout(self.layout)
		self.setLayout(self.tabx)

	
	def calculeaza_rezultatul(self):


		if self.var_1.text().isEmpty() and self.var_2.text() and self.var_3.text() and self.var_4.text():
			variabila=(float(self.var_3.text())*float(self.var_4.text()))/float(self.var_2.text())
			self.result.setText('%s' % variabila)


		elif self.var_2.text().isEmpty() and self.var_1.text() and self.var_3.text() and self.var_4.text():
			variabila=(float(self.var_3.text())*float(self.var_4.text())/float(self.var_1.text()))
			self.result.setText('%s' % variabila)


		elif self.var_3.text().isEmpty() and self.var_1.text() and self.var_2.text() and self.var_4.text():
			variabila=(float(self.var_1.text())*float(self.var_2.text())/float(self.var_4.text()))
			self.result.setText('%s' % variabila)


		elif self.var_4.text().isEmpty() and self.var_1.text() and self.var_2.text() and self.var_3.text():
			variabila=(float(self.var_1.text())*float(self.var_2.text())/float(self.var_3.text()))
			self.result.setText('%s' % variabila)


		elif self.var_1.text() and self.var_2.text() and self.var_3.text() and self.var_4.text():
			self.result.setText('%s' % txt)	


		elif self.var_1.text().isEmpty() and self.var_2.text().isEmpty and self.var_3.text() and self.var_4.text():
			self.result.setText("<font color='red'>Atentie!: Ai completat doar 2 casute</font>")

		
		elif self.var_1.text() and self.var_2.text() and self.var_3.text().isEmpty() and self.var_4.text().isEmpty():
			self.result.setText("<font color='red'>Atentie!: Ai completat doar 2 casute</font>")


		elif self.var_1.text() and self.var_2.text().isEmpty() and self.var_3.text().isEmpty() and self.var_4.text():
			self.result.setText("<font color='red'>Atentie!: Ai completat doar 2 casute</font>")	


		elif self.var_1.text().isEmpty() and self.var_2.text() and self.var_3.text() and self.var_4.text().isEmpty():
			self.result.setText("<font color='red'>Atentie!: Ai completat doar 2 casute</font>")	

		
		elif self.var_1.text() and self.var_2.text().isEmpty() and self.var_3.text() and self.var_4.text().isEmpty():
			self.result.setText("<font color='red'>Atentie!: Ai completat doar 2 casute</font>")


		elif self.var_1.text().isEmpty() and self.var_2.text() and self.var_3.text().isEmpty() and self.var_4.text():
			self.result.setText("<font color='red'>Atentie!: Ai completat doar 2 casute</font>")


		elif self.var_1.text().isEmpty() and self.var_2.text().isEmpty() and self.var_3.text().isEmpty() and self.var_4.text().isEmpty():
			self.result.setText('%s' % avertizment)



	def run(self):
		self.show()
		qt_app.exec_()

app=LayoutExample()
app.run()













