# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Set-config.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class setConfig(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_5)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(190, 50, 173, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(9, 50, 174, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(lambda: Form.close())
        self.pushButton.clicked.connect(lambda: self.testsignal())
        self.comboBox.setCurrentIndex(1)
        self.comboBox_2.setCurrentIndex(2)
        self.comboBox_3.setCurrentIndex(1)

    def testsignal(self):
        pilihIR = self.comboBox.currentIndex()
        pilihLPF = self.comboBox_2.currentIndex()
        pilihHPF = self.comboBox_3.currentIndex()
        print(self.comboBox_4.currentIndex())
        print(self.comboBox_5.currentIndex())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set Config"))
        self.comboBox.setItemText(0, _translate("Form", "2G"))
        self.comboBox.setItemText(1, _translate("Form", "4G"))
        self.comboBox.setItemText(2, _translate("Form", "8G"))
        self.comboBox_2.setItemText(0, _translate("Form", "26HZ"))
        self.comboBox_2.setItemText(1, _translate("Form", "52HZ"))
        self.comboBox_2.setItemText(2, _translate("Form", "104HZ"))
        self.comboBox_2.setItemText(3, _translate("Form", "209HZ"))
        self.comboBox_2.setItemText(4, _translate("Form", "418HZ"))
        self.comboBox_2.setItemText(5, _translate("Form", "800HZ"))
        self.comboBox_4.setItemText(0, _translate("Form", "ENABLE"))
        self.comboBox_4.setItemText(1, _translate("Form", "DISABLE"))
        self.comboBox_3.setItemText(0, _translate("Form", "g"))
        self.comboBox_3.setItemText(1, _translate("Form", "mili g"))
        self.comboBox_3.setItemText(2, _translate("Form", "f*t/s^2"))
        self.comboBox_3.setItemText(3, _translate("Form", "m/s^2"))
        self.label.setText(_translate("Form", "Input Range"))
        self.label_2.setText(_translate("Form", "Low Pass Filter"))
        self.label_3.setText(_translate("Form", "High Pass Filter"))
        self.comboBox_5.setCurrentText(_translate("Form", "Choose Channel"))
        self.comboBox_5.setItemText(0, _translate("Form", "Choose Channel"))
        self.comboBox_5.setItemText(1, _translate("Form", "CH1"))
        self.comboBox_5.setItemText(2, _translate("Form", "CH2"))
        self.comboBox_5.setItemText(3, _translate("Form", "CH3"))
        self.pushButton.setText(_translate("Form", "Apply"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton_2.clicked.connect(lambda: Form.close())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = setConfig()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
