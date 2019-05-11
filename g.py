from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import datetime

# Connect 2 Arduino with serial port
# ser = serial.Serial('COM6', 9600)
# ser = serial.Serial(port='/dev/tty.usbmodem14201', baudrate=9600)


# Connect w/ Bluetooth tty.HC-06-SPPDev
port="/dev/tty.HC-06-SPPDev" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick


# //GUI START
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 401, 131))
        self.label.setStyleSheet("font: 28pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(610, 50, 121, 121))
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 190, 121, 251))
        self.label_2.setStyleSheet("font: 28pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>DC MOTORs</p><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">DC MOTOR POSITION:</p></body></html>"))
        self.lcdNumber.setToolTip(_translate("MainWindow", "<html><head/><body><p>90</p></body></html>"))
#         self.lcdNumber.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
       
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">90</span></p></body></html>"))
         
        # self.label_2.setText(str(MPosition))
        
       
        # self.lcdNumber.display(MPosition)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def update_label():
        # tmp = ser.readline()
        # decTmp = str(tmp, 'utf-8')

        tmp = bluetooth.readline()
        decTmp = str(tmp, 'utf-8')wu
        
        # position = str(datetime.datetime.now().time())
        ui.label_2.setText(decTmp)
        ui.lcdNumber.display(decTmp)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  # every 1,000 millisecond

    sys.exit(app.exec_())
