 def openWindow1(self):
        self.window = QtWidgets.QWidget()
        self.bb = samplingNetwork()
        self.bb.setupUi(self.window)
        self.window.show()