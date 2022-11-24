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
import mscl
import csv

config = mscl.WirelessNodeConfig()
class MainWindow(QMainWindow):

    # def setConfig(node):
    #     config.defaultMode(mscl.WirelessTypes.defaultMode_idle)
    #     config.inactivityTimeout(7200)
    #     config.unlimitedDuration(True)
    #     config.samplingMode(mscl.WirelessTypes.samplingMode_sync)
    #     config.dataFormat(mscl.WirelessTypes.dataFormat_cal_float)
    def enableBeacon(self):
        try:
            # make sure we can ping the base station
            if not self.baseStation.ping():
                print("Failed to ping the Base Station")

            if self.baseStation.features().supportsBeaconStatus():
                status = self.baseStation.beaconStatus()
                print("Beacon current status: Enabled?", status.enabled(), "Time:", status.timestamp())
                print("Attempting to enable the beacon...")

            # enable the beacon on the Base Station using the PC time
            startTime = self.baseStation.enableBeacon()

            # if we got here, no exception was thrown, so enableBeacon was successful
            print("Successfully enabled the beacon on the Base Station")
            print("Beacon's initial Timestamp:", startTime)
        except Exception:
            print("Error Beacon :", Exception._str_) 


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
    def setting(self):
        IP_ADDRESS = self.ui.ipEdit.text
        tcpConnection = mscl.Connection.TcpIp(IP_ADDRESS, 5000)
        baseStation = mscl.BaseStation(tcpConnection)
        NODE_ADDRESS = self.ui.nodeEdit.text
        node = mscl.WirelessNode(NODE_ADDRESS, baseStation)
    def update_plot_data(self):
        arrDataCH1 = []
        arrDataCH2 = []
        arrDataCH3 = []
        tempTimestamp = 0

        sweeps = self.baseStation.getData(1)
        print(len(sweeps))
        for sweep in sweeps:                    
            i=0 
            print("len sweep data ",len(sweep.data()))
            tempTimestamp = str(sweep.timestamp())
            for dataPoint in sweep.data():                  
                
                i+=1
                if i is 1:
                    arrDataCH1.append(dataPoint.as_float())
                elif i is 2:
                    arrDataCH2.append(dataPoint.as_float()) 
                elif i is 3:
                    arrDataCH3.append(dataPoint.as_float())
                            

            self.x = self.x[1:]  # Remove the first y element.
            self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
            
            #DATA1
            self.y1 = self.y1[1:]  # Remove the first
            self.y1.append(arrDataCH1[-1])  # Add a new random value.
            self.DataLine1.setData(self.x, self.y1)  # Update the data.

            #DATA2
            self.y2 = self.y2[1:]  # Remove the first
            self.y2.append(arrDataCH2[-1])  # Add a new random value.
            self.DataLine2.setData(self.x, self.y2)  # Update the data.

            #DATA3
            self.y3 = self.y3[1:]  # Remove the first
            self.y3.append(arrDataCH3[-1])  # Add a new random value.
            self.DataLine3.setData(self.x, self.y3)  # Update the data.

            all_data = tempTimestamp+","+dataPoint.as_string()
            sensor_data_parsing = all_data.split(",")
            with open('sensor_output_glink.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(sensor_data_parsing)
                csvFile.close()
    def draw1(self):    
        self.x = list(range(1024))  # 100 time points
        self.y1 = [0 for _ in range(1024)]  # 100 data points
        self.y2 = [0 for _ in range(1024)]  # 100 data points
        self.y3 = [0 for _ in range(1024)]  # 100 data points

        self.ui.nodeGraph_1.showGrid(x=True, y=True)

        self.tcpConnection = mscl.Connection.TcpIp(self.IP_ADDRESS, 5000)
        self.baseStation = mscl.BaseStation(self.tcpConnection)

        self.DataLine1 = self.ui.nodeGraph_1.plot(self.x, self.y1, pen='r') #CH1 
        self.DataLine2 = self.ui.nodeGraph_1.plot(self.x, self.y2, pen='g') #CH2
        self.DataLine3 = self.ui.nodeGraph_1.plot(self.x, self.y3, pen='b') #CH3
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
    def draw2(self):    
        self.x = list(range(1024))  # 100 time points
        self.y1 = [0 for _ in range(1024)]  # 100 data points
        self.y2 = [0 for _ in range(1024)]  # 100 data points
        self.y3 = [0 for _ in range(1024)]  # 100 data points

        self.ui.nodeGraph_1.showGrid(x=True, y=True)

        self.tcpConnection = mscl.Connection.TcpIp(self.IP_ADDRESS, 5000)
        self.baseStation = mscl.BaseStation(self.tcpConnection)

        self.DataLine1 = self.ui.nodeGraph_2.plot(self.x, self.y1, pen='r') #CH1 
        self.DataLine2 = self.ui.nodeGraph_2.plot(self.x, self.y2, pen='g') #CH2
        self.DataLine3 = self.ui.nodeGraph_2.plot(self.x, self.y3, pen='b') #CH3
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
    def draw3(self):    
        self.x = list(range(1024))  # 100 time points
        self.y1 = [0 for _ in range(1024)]  # 100 data points
        self.y2 = [0 for _ in range(1024)]  # 100 data points
        self.y3 = [0 for _ in range(1024)]  # 100 data points

        self.ui.nodeGraph_1.showGrid(x=True, y=True)

        self.tcpConnection = mscl.Connection.TcpIp(self.IP_ADDRESS, 5000)
        self.baseStation = mscl.BaseStation(self.tcpConnection)

        self.DataLine1 = self.ui.nodeGraph_3.plot(self.x, self.y1, pen='r') #CH1 
        self.DataLine2 = self.ui.nodeGraph_3.plot(self.x, self.y2, pen='g') #CH2
        self.DataLine3 = self.ui.nodeGraph_3.plot(self.x, self.y3, pen='b') #CH3
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
    def draw4(self):    
        self.x = list(range(1024))  # 100 time points
        self.y1 = [0 for _ in range(1024)]  # 100 data points
        self.y2 = [0 for _ in range(1024)]  # 100 data points
        self.y3 = [0 for _ in range(1024)]  # 100 data points

        self.ui.nodeGraph_1.showGrid(x=True, y=True)

        self.tcpConnection = mscl.Connection.TcpIp(self.IP_ADDRESS, 5000)
        self.baseStation = mscl.BaseStation(self.tcpConnection)

        self.DataLine1 = self.ui.nodeGraph_4.plot(self.x, self.y1, pen='r') #CH1 
        self.DataLine2 = self.ui.nodeGraph_4.plot(self.x, self.y2, pen='g') #CH2
        self.DataLine3 = self.ui.nodeGraph_4.plot(self.x, self.y3, pen='b') #CH3
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def inputcombo1(node):
        sRInputUser = int(node.bb.comboBox.currentIndex())
        if sRInputUser == 0 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_1Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 1 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_2Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 2 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_4Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 3 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_8Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 4 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_16Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 5 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_32Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 6 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_64Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 7 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_128Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 8 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_256Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif sRInputUser == 9 :
            config.sampleRate(mscl.WirelessTypes.sampleRate_512Hz)
            node.applyConfig(config)
            samplingNetwork(node) 
    def inputcombo2(node):
        DCInputUser = node.bb.comboBox_2.currentIndex()
        if DCInputUser == 0:
            config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_logAndTransmit)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif DCInputUser == 1:
            config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_logOnly)
            node.applyConfig(config)
            samplingNetwork(node) 
        elif DCInputUser == 2:
            config.dataCollectionMethod(mscl.WirelessTypes.collectionMethod_transmitOnly)
            node.applyConfig(config)
            samplingNetwork(node)
    def applySampling(node):
        network = mscl.SyncSamplingNetwork(node.baseStation)
        network.addNode(node)
        network.applyConfiguration()
        network.startSampling()
        samplingNetwork(node)  
    def buttonwindow1(self):
        self.inputcombo1()
        self.inputcombo2()
        self.applySampling()
        self.close()
    def inputbox(node):
        pilihIR = node.aa.comboBox.currentIndex()
        accelChannelMaskIR = mscl.ChannelMask(7)
        if pilihIR == 0:
            config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_2G)
            node.applyConfig(config)
            setConfig(node)
        elif pilihIR == 1:
            config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_4G)
            node.applyConfig(config)
            setConfig(node)
        elif pilihIR == 2:
            config.inputRange(accelChannelMaskIR, mscl.WirelessTypes.range_8G)
            node.applyConfig(config)
            setConfig(node)
    
    def lowPassFilter(node):
        pilihLPF = int(node.aa.comboBox_2.currentIndex())
        accelChannelMaskLPF = mscl.ChannelMask(7)
        if pilihLPF == 0:
            config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_26hz)
            node.applyConfig(config)
            setConfig(node)
        elif pilihLPF == 1:
            config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_52hz)
            node.applyConfig(config)
            setConfig(node)
        elif pilihLPF == 2:
            config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_104hz)       
            node.applyConfig(config)
            setConfig(node)
        elif pilihLPF == 3:
            config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_209hz)
            node.applyConfig(config)
            setConfig(node)              
        elif pilihLPF == 4:
            config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_418hz) 
            node.applyConfig(config)
            setConfig(node)           
        elif pilihLPF == 5:
            config.lowPassFilter(accelChannelMaskLPF, mscl.WirelessTypes.filter_800hz)
            node.applyConfig(config)
            setConfig(node)

    def highPassFilter(node):
        accelChannelMaskHPF = mscl.ChannelMask(7)
        pilihHPF= int(node.aa.comboBox_3.currentIndex())
        if pilihHPF == 1:
            config.highPassFilter(accelChannelMaskHPF, mscl.WirelessTypes.highPass_auto)
            node.applyConfig(config)
            setConfig(node)
        if pilihHPF == 2:
            config.highPassFilter(accelChannelMaskHPF, mscl.WirelessTypes.highPass_off)
            node.applyConfig(config)
            setConfig(node)
    
    def calCoef(node):
        accelChannelMaskCh1 = mscl.ChannelMask(1) 
        accelChannelMaskCh2 = mscl.ChannelMask(2)
        accelChannelMaskCh3 = mscl.ChannelMask(4)
        pilihCH = int(node.aa.comboBox_4.currentIndex)
        if pilihCH == 0:
            pilihUnitCH1 = int(node.aa.comboBox_5.currentIndex)
            if pilihUnitCH1 == 1:
                config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_g)
                node.applyConfig(config)
                node.calibrationConfig(node)
            elif pilihUnitCH1 == 2:
                config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_milliG)    
                node.applyConfig(config) 
                node.calibrationConfig(node)
            elif pilihUnitCH1 == 3:
                config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_ftPerSec2)          
                node.applyConfig(config)
                node.calibrationConfig(node)
            elif pilihUnitCH1 == 4:
                config.unit(accelChannelMaskCh1, mscl.WirelessTypes.unit_accel_mPerSec2)             
                node.applyConfig(config)
                node.calibrationConfig(node)
        if pilihCH == 1:
            pilihUnitCH2 = int(node.aa.comboBox_5.currentIndex)
            if pilihUnitCH2 == 1:
                config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_g)
                node.applyConfig(config)
                node.calibrationConfig(node)
            elif pilihUnitCH2 == 2:
                config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_milliG)
                node.applyConfig(config) 
                node.calibrationConfig(node)   
            elif pilihUnitCH2 == 3:
                config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_ftPerSec2)
                node.applyConfig(config)  
                node.calibrationConfig(node)        
            elif pilihUnitCH2 == 4:
                config.unit(accelChannelMaskCh2, mscl.WirelessTypes.unit_accel_mPerSec2)  
                node.applyConfig(config)
                node.calibrationConfig(node)
        if pilihCH == 2:
            pilihUnitCH3 = int(node.aa.comboBox_5.currentIndex)
            if pilihUnitCH3 == 1:
                config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_g)
                node.applyConfig(config)
                node.calibrationConfig(node)
            elif pilihUnitCH3 == 2:
                config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_milliG)
                node.applyConfig(config) 
                node.calibrationConfig(node)  
            elif pilihUnitCH3 == 3:
                config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_ftPerSec2)
                node.applyConfig(config)  
                node.calibrationConfig(node)        
            elif pilihUnitCH3 == 4:
                config.unit(accelChannelMaskCh3, mscl.WirelessTypes.unit_accel_mPerSec2)
                node.applyConfig(config)     
                node.calibrationConfig(node)          
        
    def buttonset(self):
        self.inputbox()
        self.lowPassFilter()
        self.highPassFilter()
        self.calCoef()
        self.close()
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
        self.ui.checkButton.clicked.connect(self.setting())
        self.bb.pushButton.clicked.connect(self.buttonwindow1())
        self.aa.pushButton.clicked.connect(self.buttonset ())
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
        self.ui.node2Button_3.clicked.connect(lambda: self.openWindow2())

        self.ui.node3Button_1.clicked.connect(lambda: self.openWindow1())
        self.ui.node3Button_3.clicked.connect(lambda: self.openWindow2())

        #graph functions
        self.ui.nodeGraph_1.hide()
        self.ui.graphLabel_1.hide()
        self.ui.graphButton_1.pressed.connect(lambda: self.ui.graphLabel_1.show())
        self.ui.graphButton_1.pressed.connect(lambda: self.ui.nodeGraph_1.show())
        self.ui.graphButton_1.clicked.connect(lambda: self.ui.nodeGraph_1.hide())
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