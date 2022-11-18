from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from cobain import *
# IMPORT FUNCTIONS
from SNWindow import Ui_Sampling
from Setconfig import setConfig

class MainWindow(QMainWindow):
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Sampling()
        self.ui.setupUi(self.window)
        self.window.show

    def openWindow2(self):
        self.window = QtWidgets.QWidget()
        self.ui = setConfig
        self.ui.setupUi(self.window)
        self.window.show

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PAGES
        ########################################################################

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
        
        self.ui.node1Button_1.clicked.connect(lambda: self.openWindow1())
        
        self.ui.node1Button_3.clicked.connect(lambda: self.openWindow2)

        self.ui.node1Button_4.clicked.connect(lambda: self.draw1())
       ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    def draw1(self):
        self.x = list(range(1024))  # 100 time points
        self.y1 = [0 for _ in range(1024)]  # 100 data points
        self.y2 = [0 for _ in range(1024)]  # 100 data points
        self.y3 = [0 for _ in range(1024)]  # 100 data points

        self.nodeGraph_1.showGrid(x=True, y=True)

        self.tcpConnection = mscl.Connection.TcpIp(IP_ADDRESS, 5000)
        self.baseStation = mscl.BaseStation(self.tcpConnection)

        self.DataLine1 = self.nodeGraph_1.plot(self.x, self.y1, pen='r') #CH1 
        self.DataLine2 = self.nodeGraph_1.plot(self.x, self.y2, pen='g') #CH2
        self.DataLine3 = self.nodeGraph_1.plot(self.x, self.y3, pen='b') #CH3
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def activity():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())