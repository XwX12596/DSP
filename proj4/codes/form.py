# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.freq_lb = QtWidgets.QLabel(Form)
        self.freq_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.freq_lb.setObjectName("freq_lb")
        self.gridLayout.addWidget(self.freq_lb, 0, 1, 1, 1)
        self.freq_le = QtWidgets.QLineEdit(Form)
        self.freq_le.setObjectName("freq_le")
        self.gridLayout.addWidget(self.freq_le, 0, 2, 1, 1)
        self.start = QtWidgets.QPushButton(Form)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 1, 0, 1, 1)
        self.p1 = QtWidgets.QPushButton(Form)
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 1, 1, 1, 2)
        self.p10 = QtWidgets.QPushButton(Form)
        self.p10.setObjectName("p10")
        self.gridLayout.addWidget(self.p10, 1, 3, 1, 1)
        self.m1 = QtWidgets.QPushButton(Form)
        self.m1.setObjectName("m1")
        self.gridLayout.addWidget(self.m1, 3, 0, 1, 1)
        self.p100 = QtWidgets.QPushButton(Form)
        self.p100.setObjectName("p100")
        self.gridLayout.addWidget(self.p100, 2, 0, 1, 1)
        self.p1000 = QtWidgets.QPushButton(Form)
        self.p1000.setObjectName("p1000")
        self.gridLayout.addWidget(self.p1000, 2, 1, 1, 2)
        self.p10000 = QtWidgets.QPushButton(Form)
        self.p10000.setObjectName("p10000")
        self.gridLayout.addWidget(self.p10000, 2, 3, 1, 1)
        self.m10 = QtWidgets.QPushButton(Form)
        self.m10.setObjectName("m10")
        self.gridLayout.addWidget(self.m10, 3, 1, 1, 2)
        self.m100 = QtWidgets.QPushButton(Form)
        self.m100.setObjectName("m100")
        self.gridLayout.addWidget(self.m100, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.freq_lb.setText(_translate("Form", "frequency"))
        self.start.setText(_translate("Form", "Start"))
        self.p1.setText(_translate("Form", "+1Hz"))
        self.p10.setText(_translate("Form", "+10Hz"))
        self.m1.setText(_translate("Form", "-1Hz"))
        self.p100.setText(_translate("Form", "+100Hz"))
        self.p1000.setText(_translate("Form", "+1000Hz"))
        self.p10000.setText(_translate("Form", "+10000Hz"))
        self.m10.setText(_translate("Form", "-10Hz"))
        self.m100.setText(_translate("Form", "-100Hz"))
