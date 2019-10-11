from lcd_time import *
import sys
import time
import threading
i=0
h=0
m=0
s=0

class tApp(Ui_MainWindow):

	def __init__(self,window):

		self.setupUi(window)
		self.quit.clicked.connect(self.exit)
		self.start.clicked.connect(self.tim)
		self.t1.clicked.connect(self.task1)
		self.t2.clicked.connect(self.task2)
		self.t3.clicked.connect(self.task3)



	def exit(self):
		sys.exit()

	def tim(self):
		t1=threading.Thread(target=self.timer)
		t1.start()

	def timer(self):
		global i
		global num
		global h
		global m
		global s

		while i>=0:
			m,s=divmod(i,60)
			h,m=divmod(m,60)
			self.lcdNumber.display(str(h).zfill(2) +':'+str(m).zfill(2)+':'+str(s).zfill(2))
			i=i+1
			time.sleep(1)

	def task1(self):
		global h
		global m
		global s
		self.lcdNumber_1.display(str(h).zfill(2) +':'+str(m).zfill(2)+':'+str(s).zfill(2))
	def task2(self):
		global h
		global m
		global s
		self.lcdNumber_2.display(str(h).zfill(2) +':'+str(m).zfill(2)+':'+str(s).zfill(2))
	def task3(self):
		global i
		global h
		global m
		global s
		self.lcdNumber_3.display(str(h).zfill(2) +':'+str(m).zfill(2)+':'+str(s).zfill(2))
		i=-1

app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=tApp(MainWindow)
MainWindow.show()
app.exec_()