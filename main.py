from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from MainWindow import Ui_MainWindow
from random import randint
# IMPORT FUNCTIONS
from Samplingnetwork import samplingNetwork
#from cobain import *
from Setconfig import setConfig

class MainWindow(QMainWindow):
    # def setConfig(node):
    #     config.defaultMode(mscl.WirelessTypes.defaultMode_idle)
    #     config.inactivityTimeout(7200)
    #     config.unlimitedDuration(True)
    #     config.samplingMode(mscl.WirelessTypes.samplingMode_sync)
    #     config.dataFormat(mscl.WirelessTypes.dataFormat_cal_float)
    # def enableBeacon(self):
    #     try:
    #         # make sure we can ping the base station
    #         if not self.baseStation.ping():
    #             print("Failed to ping the Base Station")

    #         if self.baseStation.features().supportsBeaconStatus():
    #             status = self.baseStation.beaconStatus()
    #             print("Beacon current status: Enabled?", status.enabled(), "Time:", status.timestamp())
    #             print("Attempting to enable the beacon...")

    #         # enable the beacon on the Base Station using the PC time
    #         startTime = self.baseStation.enableBeacon()

    #         # if we got here, no exception was thrown, so enableBeacon was successful
    #         print("Successfully enabled the beacon on the Base Station")
    #         print("Beacon's initial Timestamp:", startTime)
    #     except Exception:
    #         print("Error Beacon :", Exception._str_) 

    def textinput(self):
        IPaddress = self.ui.ipEdit.text()
        NODE_ADDRESS = self.ui.nodeEdit.text()
        print(IPaddress)
        print(NODE_ADDRESS)
    ##open window for sampling network
    def openWindow1(self):
        self.window = QtWidgets.QWidget()
        self.bb = samplingNetwork()
        self.bb.setupUi(self.window)
        self.window.show()

    ##open window for setting configuration
    def openWindow2(self):
        self.window = QtWidgets.QWidget()
        self.aa = setConfig()
        self.aa.setupUi(self.window)
        self.window.show()  

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        ## FUNCTIONS


        #tcpConnection = mscl.Connection.TcpIp(IPaddress, 5000)
        #baseStation = mscl.BaseStation(tcpConnection)
        #node = mscl.WirelessNode(NODE_ADDRESS, baseStation)

        ## PAGES
        ########################################################################
        #home page
        self.ui.checkButton.clicked.connect(lambda: self.textinput())
        # PAGE 1
        self.ui.activityButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Activity))

        # PAGE 2
        self.ui.homeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))

        # PAGE 3
        self.ui.devicesButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Devices))

        #devices page
        self.ui.baseButton.clicked.connect(lambda: self.ui.devicePage.setCurrentWidget(self.ui.base_Page))
        self.ui.node1Button.clicked.connect(lambda: self.ui.devicePage.setCurrentWidget(self.ui.node_1))
        self.ui.node2Button.clicked.connect(lambda: self.ui.devicePage.setCurrentWidget(self.ui.node_2))
        self.ui.node3Button.clicked.connect(lambda: self.ui.devicePage.setCurrentWidget(self.ui.node_3))
        
        #Node windows
        self.ui.node1Button_1.clicked.connect(lambda: self.openWindow1())
        self.ui.node1Button_3.clicked.connect(lambda: self.openWindow2())

        self.ui.node2Button_1.clicked.connect(lambda: self.openWindow1())

        #graph functions
        self.ui.nodeGraph_1.hide()
        self.ui.graphLabel_1.hide()
        self.ui.graphButton_1.pressed.connect(lambda: self.ui.graphLabel_1.show())
        self.ui.graphButton_1.pressed.connect(lambda: self.ui.nodeGraph_1.show())
        self.ui.graphLabel_2.hide()
        self.ui.graphButton_2.pressed.connect(lambda: self.ui.graphLabel_2.show())
        self.ui.nodeGraph_2.hide()
        self.ui.graphButton_2.pressed.connect(lambda: self.ui.nodeGraph_2.show())
        self.ui.graphLabel_3.hide()
        self.ui.graphButton_3.pressed.connect(lambda: self.ui.graphLabel_3.show())
        self.ui.nodeGraph_3.hide()
        self.ui.graphButton_3.pressed.connect(lambda: self.ui.nodeGraph_3.show())
        self.ui.graphLabel_4.hide()
        self.ui.graphButton_4.pressed.connect(lambda: self.ui.graphLabel_4.show())
        self.ui.nodeGraph_4.hide()
        self.ui.graphButton_4.pressed.connect(lambda: self.ui.nodeGraph_4.show())   
        
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())