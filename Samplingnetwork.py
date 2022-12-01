# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sampling-network.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class SamplingNetworkClass(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelbutton = QtWidgets.QPushButton(self.frame_3)
        self.cancelbutton.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.cancelbutton)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 2) 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.cancelbutton.clicked.connect(lambda: Form.close())
        self.comboBox.setCurrentIndex(8)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Samping Network"))
        self.label.setText(_translate("Form", "Sampling Rate"))
        self.label_2.setText(_translate("Form", "Data Collect"))
        self.comboBox.setItemText(0, _translate("Form", "1 HZ"))
        self.comboBox.setItemText(1, _translate("Form", "2 HZ"))
        self.comboBox.setItemText(2, _translate("Form", "4 HZ"))
        self.comboBox.setItemText(3, _translate("Form", "8 HZ"))
        self.comboBox.setItemText(4, _translate("Form", "16 HZ"))
        self.comboBox.setItemText(5, _translate("Form", "32 HZ"))
        self.comboBox.setItemText(6, _translate("Form", "64 HZ"))
        self.comboBox.setItemText(7, _translate("Form", "128 HZ"))
        self.comboBox.setItemText(8, _translate("Form", "256 HZ"))
        self.comboBox.setItemText(9, _translate("Form", "512 HZ"))
        self.comboBox_2.setItemText(0, _translate("Form", "Log and Transmit"))
        self.comboBox_2.setItemText(1, _translate("Form", "Log Only"))
        self.comboBox_2.setItemText(2, _translate("Form", "Transmit Only"))
        self.cancelbutton.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SamplingNetworkClass()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
