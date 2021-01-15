# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(200, 139, 113, 31))
        self.input.setObjectName("input")
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(360, 140, 113, 31))
        self.output.setObjectName("output")
        self.findcapital = QtWidgets.QPushButton(self.centralwidget)
        self.findcapital.setGeometry(QtCore.QRect(200, 190, 75, 31))
        self.findcapital.setObjectName("findcapital")
        self.findupper = QtWidgets.QPushButton(self.centralwidget)
        self.findupper.setGeometry(QtCore.QRect(300, 190, 71, 31))
        self.findupper.setObjectName("findupper")
        self.findlower = QtWidgets.QPushButton(self.centralwidget)
        self.findlower.setGeometry(QtCore.QRect(400, 190, 75, 31))
        self.findlower.setObjectName("findlower")
        self.findstring = QtWidgets.QPushButton(self.centralwidget)
        self.findstring.setGeometry(QtCore.QRect(200, 240, 75, 31))
        self.findstring.setObjectName("findstring")
        self.findnumber = QtWidgets.QPushButton(self.centralwidget)
        self.findnumber.setGeometry(QtCore.QRect(300, 240, 71, 31))
        self.findnumber.setObjectName("findnumber")
        self.numcount = QtWidgets.QPushButton(self.centralwidget)
        self.numcount.setGeometry(QtCore.QRect(400, 240, 75, 31))
        self.numcount.setObjectName("numcount")
        self.findspace = QtWidgets.QPushButton(self.centralwidget)
        self.findspace.setGeometry(QtCore.QRect(200, 290, 75, 30))
        self.findspace.setObjectName("findspace")
        self.findalpha = QtWidgets.QPushButton(self.centralwidget)
        self.findalpha.setGeometry(QtCore.QRect(300, 290, 75, 30))
        self.findalpha.setObjectName("findalpha")
        self.finddigit = QtWidgets.QPushButton(self.centralwidget)
        self.finddigit.setGeometry(QtCore.QRect(400, 289, 75, 31))
        self.finddigit.setObjectName("finddigit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.findcapital.clicked.connect(self.fcapital)
        self.findupper.clicked.connect(self.fupper)
        self.findlower.clicked.connect(self.flower)
        self.finddigit.clicked.connect(self.fdigit)
        self.findalpha.clicked.connect(self.falpha)
        self.findnumber.clicked.connect(self.fnumber)
        self.findstring.clicked.connect(self.fstring)
        self.findspace.clicked.connect(self.fspace)
        self.numcount.clicked.connect(self.fcount)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def fcapital(self):
        str1=self.input.text()
        if str1.isalpha():
            self.output.setText(str1.capitalize())
        else:
            self.output.setText("Non-alpha can't be capitalize")
    def fupper(self):
        str1=self.input.text()
        if str1.isalpha():
            self.output.setText(str1.upper())
        else:
            self.output.setText("Non-alpha can't be change is Upper Case")
    def flower(self):
        str1=self.input.text()
        if str1.isalpha():
            self.output.setText(str1.lower())
        else:
            self.output.setText("Non-alpha can't be change in Lower Case")
    def fstring(self):
        str1=self.input.text()
        if str1.isalpha():
            self.output.setText("TRUE")
        else:
            self.output.setText("FALSE")

    def falpha(self):
        str1=self.input.text()
        if str1.isalpha():
            self.output.setText("TRUE")
        else:
            self.output.setText("FALSE")

    def fspace(self):
        str1=self.input.text()
        count=str1.count(" ")
        self.output.setText(str(count))
    
    def fnumber(self):
        str1=self.input.text()
        if str1.isnumeric():
            self.output.setText("TRUE")
        else:
            self.output.setText("FALSE")

    def fdigit(self):
        str1=self.input.text()
        if str1.isdigit():
            self.output.setText("TRUE")
        else:
            self.output.setText("FALSE")
    def fcount(self):
        str1=self.input.text()
        count=len(str1)
        self.output.setText(str(count))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.findcapital.setText(_translate("MainWindow", "Capitalize"))
        self.findupper.setText(_translate("MainWindow", "Upper"))
        self.findlower.setText(_translate("MainWindow", "Lower"))
        self.findstring.setText(_translate("MainWindow", "IsSrting"))
        self.findnumber.setText(_translate("MainWindow", "IsNumber"))
        self.numcount.setText(_translate("MainWindow", "Count"))
        self.findspace.setText(_translate("MainWindow", "Space"))
        self.findalpha.setText(_translate("MainWindow", "IsAlpha"))
        self.finddigit.setText(_translate("MainWindow", "IsDigit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
